from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_DIR = BASE_DIR / "knowledge"
CHROMA_DIR = BASE_DIR / "chroma_db"

COLLECTION_NAME = "code-review-guidelines"


def load_documents():
    documents = []

    for file_path in KNOWLEDGE_DIR.rglob("*.md"):
        loader = TextLoader(str(file_path), encoding="utf-8")
        loaded_documents = loader.load()

        for document in loaded_documents:
            relative_path = file_path.relative_to(KNOWLEDGE_DIR)

            document.metadata["source"] = str(relative_path)
            document.metadata["category"] = relative_path.parts[0]

            documents.append(document)

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    return splitter.split_documents(documents)


def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )

    return vector_store


def main():
    print("Loading knowledge documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    print("Splitting documents...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings and storing vectors in Chroma...")
    create_vector_store(chunks)

    print(f"Chroma database created at: {CHROMA_DIR}")


if __name__ == "__main__":
    main()