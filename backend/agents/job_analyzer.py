import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def clean_job_text(raw_text: str) -> str:
    """
    Uses Gemini to strip away 'About the Company', 'Cookie Policy', and 'Related Jobs'.
    Returns ONLY the Responsibilities and Requirements.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY is missing!")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0, google_api_key=api_key)
    
    prompt = """
    I have scraped a job posting, but it contains noise (headers, legal disclaimers, company history).
    
    YOUR TASK:
    Extract ONLY the following sections:
    1. Job Title
    2. Key Responsibilities / Duties
    3. Requirements / Qualifications / Tech Stack
    
    Discard "About Us", "Benefits", "Equal Opportunity Statement", and "Related Jobs".
    
    RAW TEXT:
    {raw_text}
    """
    
    chain = ChatPromptTemplate.from_template(prompt) | llm | StrOutputParser()
    return chain.invoke({"raw_text": raw_text[:25000]})

# Keep this for your other endpoint if you need it
def analyze_job(job_description: str) -> str:
    return clean_job_text(job_description)