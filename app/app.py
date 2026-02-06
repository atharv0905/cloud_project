from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import engine, Base, get_db
import models
import schemas
import crud
from auth import verify_post_api_key, verify_get_api_key
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Base FastAPI Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Database tables connected and created.")
        

@app.post("/random", response_model=schemas.ExternalResponse)
async def create_random_value(
    data: schemas.ExternalCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_post_api_key),
):
    return await crud.create_external_data(db, data.data)


@app.get("/random", response_model=list[schemas.ExternalResponse])
async def get_random_values(
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_get_api_key),
):
    return await crud.get_external_data(db, limit)


@app.get("/")
def health_check():
    return {"status": "server is running"}
