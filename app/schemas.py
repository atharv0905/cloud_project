from pydantic import BaseModel
from datetime import datetime

class RandomCreate(BaseModel):
    ranint: int

class RandomResponse(RandomCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True