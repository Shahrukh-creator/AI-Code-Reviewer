from app.services.review_service import ReviewService


def main():
    review_service = ReviewService()

    code = """
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id

    try:
        result = database.execute(query)
        return result
    except:
        pass
"""

    result = review_service.review_code(
        language="python",
        code=code,
    )

    print("\nCODE REVIEW")
    print("=" * 70)

    print(result["review"].model_dump_json(indent=2))

    print("\nRAG SOURCES")
    print("=" * 70)

    for source in result["sources"]:
        print(source)


if __name__ == "__main__":
    main()