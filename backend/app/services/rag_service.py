from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"

COLLECTION_NAME = "code-review-guidelines"


class RAGService:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embeddings,
            persist_directory=str(CHROMA_DIR),
        )

    def retrieve(self, query: str, k: int = 3):
        return self.vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )

    def retrieve_context(self, query: str, k: int = 3):
        results = self.retrieve(query=query, k=k)

        context_parts = []
        sources = []

        for document, score in results:
            source = document.metadata.get("source", "unknown")
            category = document.metadata.get("category", "unknown")

            context_parts.append(
                f"""
Source: {source}
Category: {category}

{document.page_content}
""".strip()
            )

            sources.append(
                {
                    "source": source,
                    "category": category,
                    "distance": float(score),
                }
            )

        context = "\n\n---\n\n".join(context_parts)

        return context, sources