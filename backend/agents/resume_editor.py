import os
from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# --- Define the Structure we want ---
class Suggestion(BaseModel):
    section: str = Field(description="Which section this belongs to (e.g., 'Summary', 'Experience')")
    original_text: str = Field(description="The exact sentence or bullet point from the original resume")
    suggested_text: str = Field(description="The rewritten version using keywords and stronger verbs")
    reasoning: str = Field(description="Why this change is recommended")

class ResumeAnalysis(BaseModel):
    match_score: int = Field(description="A score from 0 to 100 indicating how well the resume fits the job")
    missing_keywords: List[str] = Field(description="List of 3-5 important keywords present in the job but missing in the resume")
    suggestions: List[Suggestion] = Field(description="A list of specific text improvements")

# --- The Logic ---
def compare_resume_to_job(resume_text: str, job_description: str) -> dict:
    """
    Compares resume to job and returns a structured JSON object.
    """
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY is missing!")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1, # Very low temp to ensure strict JSON adherence
        google_api_key=api_key
    )

    # Set up the parser
    parser = PydanticOutputParser(pydantic_object=ResumeAnalysis)

    template = """
    You are an expert Resume Editor and ATS Specialist.
    Analyze the Candidate's Resume against the Job Description.
    
    YOUR GOAL:
    Provide a structured analysis that helps the candidate pass the ATS (Applicant Tracking System).
    
    1. Calculate a Match Score (0-100).
    2. Identify critical Missing Keywords.
    3. Find 3-5 weak bullet points or sentences and rewrite them to be stronger, metric-driven, and aligned with the job.
    
    CRITICAL INSTRUCTION:
    - Do not hallucinate facts. Only improve existing experiences.
    - Ensure "suggested_text" is professional and impactful.
    
    --------
    JOB DESCRIPTION:
    {job_description}
    
    --------
    CANDIDATE RESUME:
    {resume_text}
    
    --------
    FORMAT INSTRUCTIONS:
    {format_instructions}
    """

    prompt = ChatPromptTemplate.from_template(template)
    
    # Inject format instructions automatically
    chain = prompt | llm | parser
    
    # Run the chain
    result = chain.invoke({
        "resume_text": resume_text,
        "job_description": job_description,
        "format_instructions": parser.get_format_instructions()
    })
    
    # Return as a dictionary (JSON compatible)
    return result.dict()