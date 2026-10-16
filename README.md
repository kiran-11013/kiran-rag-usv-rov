# Marine Research Paper RAG System

A Retrieval-Augmented Generation (RAG) application for answering questions from marine robotics research papers using LangChain, FAISS, Sentence Transformers, and Groq.

The application provides a REST API through FastAPI and supports containerized deployment using Docker and Docker Compose.

## Features

- Load and process research documents
- Generate document embeddings using `all-MiniLM-L6-v2`
- Store and search embeddings using FAISS
- Retrieve relevant research content using semantic similarity
- Generate context-aware answers using Groq (`openai/gpt-oss-20b`)
- Query documents through FastAPI REST endpoints
- Deploy the application using Docker and Docker Compose

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.12 |
| RAG framework | LangChain |
| Embedding model | Sentence Transformers |
| Vector database | FAISS |
| Language model | GPT-OSS 20B via Groq |
| API framework | FastAPI |
| Application server | Uvicorn |
| Containerization | Docker |
| Container orchestration | Docker Compose |
| Dependency management | uv |

## RAG Architecture

**Document indexing pipeline**

Research PDFs → Document Loading → Text Chunking → Sentence Transformer Embeddings → FAISS Index

**Question-answering pipeline**

User Question → FastAPI → Query Embedding → FAISS Similarity Search → Relevant Document Chunks → Groq LLM → Generated Answer

## API Endpoints

### GET /health

Checks whether the FastAPI server is running.

### POST /query

Accepts a question and retrieves relevant information from the indexed research papers.

Example request:

```json
{
  "question": "What communication are they using?",
  "top_k": 3
}
```

Example response structure:

```json
{
  "question": "What communication are they using?",
  "answer": "The generated answer based on the retrieved documents."
}
```

## Run Locally

Install dependencies:

```bash
uv sync
```

Start the API:

```bash
uv run python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

## Docker Deployment

Build and start the application:

```bash
sudo docker compose up -d --build
```

Check container status:

```bash
sudo docker compose ps
```

View application logs:

```bash
sudo docker compose logs -f
```

Stop the application:

```bash
sudo docker compose down
```

### Required Local Configuration

Before starting the application:

1. Create a `.env` file containing the required Groq API credentials.
2. Place the research documents in `data/`.
3. Prepare the FAISS index in `faiss_store/`.

Research documents, the FAISS database, and API keys are excluded from the repository. Docker Compose mounts local documents and the FAISS index at runtime.

## Current Document Set

The system is currently indexed on research papers related to USV-ROV cooperative systems, sensor fusion, tether management, and autonomous marine monitoring.

## Future Work

- Add inline source citations to generated answers
- Support conversational and multi-turn queries with history
- Experiment with larger embedding models for improved retrieval accuracy
- Add automated API tests and CI/CD pipelines
- Evaluate retrieval quality and answer faithfulness
- Implement API authentication, monitoring, and structured logging
