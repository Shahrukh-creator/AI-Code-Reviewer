from typing import List

from pydantic import BaseModel


class RetrievalRequest(BaseModel):
    query: str
    k: int = 3


class RetrievalDocument(BaseModel):
    source: str
    category: str
    distance: float
    content: str


class RetrievalResponse(BaseModel):
    documents: List[RetrievalDocument]