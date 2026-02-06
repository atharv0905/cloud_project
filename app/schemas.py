from pydantic import BaseModel
from datetime import datetime

class ExternalCreate(BaseModel):
    data: dict

class ExternalResponse(ExternalCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True