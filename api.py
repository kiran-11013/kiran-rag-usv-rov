from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.search import RAGSearch

app = FastAPI(
    title="RAG Question Answering API",
    description="LangChain RAG application using FAISS and Groq",
    version="1.0.0"
)


# Define the request structure
class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


# Initialize the RAG system once
rag_search = RAGSearch()


@app.get("/")
def home():
    return {"message": "Welcome to my RAG API"}


@app.get("/health")
def health():
    return {"status": "running"}


@app.post("/query")
def query_rag(request: QueryRequest):
    try:
        answer = rag_search.search_and_summarize(
            request.question,
            top_k=request.top_k
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="RAG query failed. Check server logs."
        )