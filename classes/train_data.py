from typing import List
from pydantic import BaseModel

class TrainData(BaseModel):
    tag: str
    patterns: List[str]
    responses: List[str]
    context: List[str]