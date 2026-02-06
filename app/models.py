from sqlalchemy import Column, Integer, DateTime, JSON
from sqlalchemy.sql import func
from database import Base

class ExternalData(Base):
    __tablename__ = "external_data"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())