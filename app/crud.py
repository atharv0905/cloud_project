from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import RandomData

async def create_random(db: AsyncSession, ranint: int):
    record = RandomData(ranint=ranint)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record

async def get_random_values(db: AsyncSession, limit: int = 50):
    result = await db.execute(
        select(RandomData)
        .order_by(RandomData.created_at.desc())
        .limit(limit)
    )
    return result.scalars().all()