from fastapi import APIRouter, HTTPException

from app.models.review_models import (
    ReviewRequest,
    ReviewResponse,
)
from app.services.review_service import ReviewService


router = APIRouter(
    prefix="/api/review",
    tags=["Code Review"],
)

review_service = ReviewService()


@router.post("", response_model=ReviewResponse)
async def review_code(request: ReviewRequest):
    try:
        result = review_service.review_code(
            language=request.language,
            code=request.code,
        )

        return result

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Code review failed: {type(exc).__name__}",
        )