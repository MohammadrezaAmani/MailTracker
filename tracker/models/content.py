from pydantic import BaseModel
from datetime import datetime
from typing import List


class ContentAdd(BaseModel):
    assets: str
    link: str


class ViewDB(BaseModel):
    ip: str
    countery: str
    created_at: datetime


class ContentDB(ContentAdd):
    user: int
    views: List(ViewDB)
    created_at: datetime
