from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

def analyze_job(job_description: str):
    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)
    prompt = ChatPromptTemplate.from_template(
        "Summarize the key qualifications, skills, and technologies in the job description:\n{job_description}"
    )
    response = llm.invoke(prompt.format(job_description=job_description))
    return {"summary": response.content}
