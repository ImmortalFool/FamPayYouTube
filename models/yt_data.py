"""
    Format the data into mongo db bson format
"""

from pydantic import BaseModel
from typing import Dict


class Thumbnails(BaseModel):
    url: str
    width: int
    height: int


class YtData(BaseModel):
    vid: str
    publishedAt: str
    title: str
    description: str
    thumbnails: Dict[str, Thumbnails]
