from app.services.rag_service import RAGService


def main():
    rag_service = RAGService()

    query = """
    Python code takes user input and directly concatenates
    it into a SQL query.
    """

    context, sources = rag_service.retrieve_context(
        query=query,
        k=3,
    )

    print("\nRETRIEVED CONTEXT")
    print("=" * 70)
    print(context)

    print("\nSOURCES")
    print("=" * 70)

    for source in sources:
        print(source)


if __name__ == "__main__":
    main()