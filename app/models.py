from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from database import Base

class RandomData(Base):
    __tablename__ = "random_data"

    id = Column(Integer, primary_key=True, index=True)
    ranint = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())