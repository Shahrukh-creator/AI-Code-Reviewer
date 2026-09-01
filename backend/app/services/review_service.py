from app.chains.code_review_chain import CodeReviewChain
from app.services.rag_service import RAGService


class ReviewService:
    def __init__(self):
        self.rag_service = RAGService()
        self.review_chain = CodeReviewChain()

    def review_code(
        self,
        language: str,
        code: str,
    ):
        retrieval_query = f"""
Review this {language} code for security, correctness,
maintainability, and code quality issues:

{code}
"""

        context, sources = self.rag_service.retrieve_context(
            query=retrieval_query,
            k=3,
        )

        review = self.review_chain.review(
            language=language,
            code=code,
            context=context,
        )

        return {
            "review": review,
            "sources": sources,
        }