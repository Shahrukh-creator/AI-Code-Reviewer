from app.models.review_models import CodeReview
from app.prompts.review_prompt import CODE_REVIEW_PROMPT
from app.services.llm_service import LLMService


class CodeReviewChain:
    def __init__(self):
        llm_service = LLMService()

        structured_llm = llm_service.get_llm().with_structured_output(
            CodeReview
        )

        self.chain = CODE_REVIEW_PROMPT | structured_llm

    def review(
        self,
        language: str,
        code: str,
        context: str,
    ) -> CodeReview:
        return self.chain.invoke(
            {
                "language": language,
                "code": code,
                "context": context,
            }
        )