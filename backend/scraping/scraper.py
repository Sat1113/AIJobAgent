import trafilatura
import requests

def scrape_job_from_url(url: str) -> str:
    """
    Fetches the main content from a URL using Trafilatura (best for article/job extraction).
    """
    try:
        # 1. Try Trafilatura (Smart extraction)
        downloaded = trafilatura.fetch_url(url)
        
        # 2. Fallback to Requests if Trafilatura fails (e.g. simple HTML sites)
        if downloaded is None:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            downloaded = response.text

        # 3. Extract main text
        text = trafilatura.extract(downloaded)

        if not text:
            raise ValueError("Could not extract main content from this URL.")

        return text.strip()[:20000] # Cap at 20k chars to save tokens

    except Exception as e:
        raise Exception(f"Scraping error: {str(e)}")