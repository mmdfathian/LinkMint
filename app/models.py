from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class URLMap(Base):
    __tablename__ = "url_maps"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

