from typing import List, Optional

from pydantic import BaseModel, Field


class ReviewIssue(BaseModel):
    severity: str = Field(
        description="Issue severity: low, medium, high, or critical"
    )
    category: str = Field(
        description="Issue category such as security, maintainability, or performance"
    )
    line: Optional[int] = Field(
        default=None,
        description="Approximate line number if identifiable"
    )
    problem: str
    explanation: str
    suggestion: str


class CodeReview(BaseModel):
    summary: str
    score: float = Field(
        ge=0,
        le=10,
        description="Overall code quality score from 0 to 10"
    )
    issues: List[ReviewIssue]
    strengths: List[str]


class ReviewRequest(BaseModel):
    language: str
    code: str


class ReviewSource(BaseModel):
    source: str
    category: str
    distance: float


class ReviewResponse(BaseModel):
    review: CodeReview
    sources: List[ReviewSource]



class ReviewRequest(BaseModel):
    language: str = Field(
        min_length=1,
        max_length=50,
        description="Programming language of the submitted code",
    )

    code: str = Field(
        min_length=1,
        max_length=20000,
        description="Source code to review",
    )


class ReviewSource(BaseModel):
    source: str
    category: str
    distance: float