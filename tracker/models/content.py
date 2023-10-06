from pydantic import BaseModel
from datetime import datetime
from typing import List

# from fastapi import Request


class ContentAdd(BaseModel):
    assets: str
    link: str


class ViewDB(BaseModel):
    id: str
    ip: str
    countery: str
    created_at: datetime
    request: dict


class ContentDB(ContentAdd):
    id: str
    user: int
    views: List[ViewDB]
    created_at: datetime
