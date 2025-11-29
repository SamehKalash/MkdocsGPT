from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from rag import get_answer
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MkDocsGPT RAG API",
    description="Retrieval-Augmented Generation API for mkdocs documents",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

class Response(BaseModel):
    answer: str
    status: str

@app.get("/", tags=["Web UI"])
def serve_ui():
    """Serve the web UI"""
    if os.path.exists("index.html"):
        return FileResponse("index.html", media_type="text/html")
    return {"message": "Web UI not found. Place index.html in the project root."}

@app.get("/api", tags=["API Redirect"])
def api_redirect():
    """Redirect to API documentation"""
    return {"message": "API documentation available at /docs or /redoc"}

@app.get("/status", tags=["Health"])
def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "MkdocsGPT RAG API",
        "version": "1.0.0"
    }

@app.post("/ask", response_model=Response, tags=["RAG"])
def ask(query: Query):
    """
    Ask a question and get an answer based on the mkdocs documents.
    
    - **question**: The question to ask
    
    Returns:
    - **answer**: The generated answer
    - **status**: Status of the request (success/error)
    """
    try:
        if not query.question or not query.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        logger.info(f"Processing question: {query.question}")
        answer = get_answer(query.question)
        logger.info("Answer generated successfully")
        
        return {
            "answer": answer,
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@app.get("/docs", tags=["Documentation"])
def docs():
    """Redirect to interactive API documentation"""
    return {"message": "Visit /docs for Swagger UI or /redoc for ReDoc"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)