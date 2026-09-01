from fastapi import APIRouter

from app.models.retrieval_models import (
    RetrievalDocument,
    RetrievalRequest,
    RetrievalResponse,
)
from app.services.rag_service import RAGService


router = APIRouter(
    prefix="/api/retrieval",
    tags=["RAG Retrieval"],
)

rag_service = RAGService()


@router.post("/search", response_model=RetrievalResponse)
async def search_knowledge(request: RetrievalRequest):
    results = rag_service.retrieve(
        query=request.query,
        k=request.k,
    )

    documents = []

    for document, score in results:
        documents.append(
            RetrievalDocument(
                source=document.metadata.get("source", "unknown"),
                category=document.metadata.get("category", "unknown"),
                distance=float(score),
                content=document.page_content,
            )
        )

    return RetrievalResponse(documents=documents)