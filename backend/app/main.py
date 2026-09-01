from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.retrieval_routes import router as retrieval_router

from app.api.review_routes import router as review_router


app = FastAPI(
    title="AI Code Reviewer",
    version="1.0.0",
    description="LLM-powered code review using LangChain, RAG, and Chroma.",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://localhost:5400",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "ai-code-reviewer",
    }


app.include_router(review_router)
app.include_router(retrieval_router)