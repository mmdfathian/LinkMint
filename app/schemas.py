from pydantic import BaseModel, HttpUrl
from datetime import datetime


class URLCreate(BaseModel):
    url: HttpUrl


class URLInfo(BaseModel):
    id: int
    original_url: str
    short_code: str
    clicks: int
    created_at: datetime
    short_url: str

    class Config:
        from_attributes = True

