import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

# Internal Imports
from agents.job_analyzer import clean_job_text
from agents.resume_editor import compare_resume_to_job
from scraping.scraper import scrape_job_from_url
from utils.file_loader import extract_text_from_pdf

load_dotenv()

app = FastAPI(title="AI Job Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Response Models (for documentation) ---
# This helps Frontend developers know what to expect
class AnalysisResponse(BaseModel):
    success: bool
    filename: str
    match_score: int
    missing_keywords: List[str]
    suggestions: List[Dict[str, str]]

@app.post("/analyze_resume_file") # response_model=AnalysisResponse (Optional, strict typing)
async def analyze_resume_file(
    file: UploadFile = File(...), 
    job_url: str = Form(...)
):
    try:
        if not os.getenv("GOOGLE_API_KEY"):
            raise HTTPException(status_code=500, detail="Google API Key missing.")

        print(f"📄 Processing: {file.filename}")

        # 1. Read PDF
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Please upload a PDF.")
            
        file_content = await file.read()
        resume_text = extract_text_from_pdf(file_content)

        if len(resume_text) < 50:
             raise HTTPException(status_code=400, detail="PDF seems empty.")

        # 2. Scrape & Clean Job
        print("🕷️ Scraping & Cleaning URL...")
        raw_job_text = scrape_job_from_url(job_url)
        clean_job_desc = clean_job_text(raw_job_text)
        
        # 3. Analyze (Now returns a Dict, not a String)
        print("🤖 Analyzing Structure...")
        analysis_data = compare_resume_to_job(resume_text, clean_job_desc)
        
        # 4. Construct Final Response
        # We flatten the response so it's easy for the Frontend to read
        return {
            "success": True,
            "filename": file.filename,
            "match_score": analysis_data["match_score"],
            "missing_keywords": analysis_data["missing_keywords"],
            "suggestions": analysis_data["suggestions"]
        }

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)