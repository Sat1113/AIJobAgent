from fastapi import FastAPI
from agents.job_analyzer import analyze_job

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Job Agent backend runningggerr"}

@app.post("/analyze")
def analyze(job_description: str):
    return {
        "job_description": job_description,
        "analysis": analyze_job(job_description)
    }
    

