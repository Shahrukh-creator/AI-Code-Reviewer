from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"

COLLECTION_NAME = "code-review-guidelines"


def main():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    query = """
    The application builds a SQL query by concatenating
    a value supplied by the user.
    """

    results = vector_store.similarity_search_with_score(
        query=query,
        k=3,
    )

    print(f"\nQuery:\n{query.strip()}\n")
    print("=" * 70)

    for index, (document, score) in enumerate(results, start=1):
        print(f"\nRESULT {index}")
        print(f"Source: {document.metadata.get('source')}")
        print(f"Category: {document.metadata.get('category')}")
        print(f"Distance: {score}")
        print("\nContent:")
        print(document.page_content)
        print("-" * 70)


if __name__ == "__main__":
    main()