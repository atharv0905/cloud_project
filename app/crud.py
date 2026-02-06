from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import ExternalData

async def create_external_data(db: AsyncSession, data: dict):
    record = ExternalData(data=data)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record

async def get_external_data(db: AsyncSession, limit: int = 10):
    result = await db.execute(
        select(ExternalData)
        .order_by(ExternalData.created_at.desc())
        .limit(limit)
    )
    return result.scalars().all()