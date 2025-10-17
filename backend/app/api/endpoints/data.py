from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ...schemas.data import DataPointCreate, DataPointResponse
from ...models.data_point import DataPoint
from ...core.security import get_current_user
from ...db.database import get_db

router = APIRouter(prefix="/data", tags=["Data"])


@router.post("/", response_model=DataPointResponse, status_code=status.HTTP_201_CREATED)
async def create_data_point(
    data: DataPointCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Create a new data point"""
    new_data = DataPoint(**data.model_dump())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


@router.get("/", response_model=List[DataPointResponse])
async def get_data_points(
    skip: int = 0,
    limit: int = 100,
    category: str = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get data points with optional filtering"""
    query = db.query(DataPoint)
    
    if category:
        query = query.filter(DataPoint.category == category)
    
    data_points = query.order_by(DataPoint.timestamp.desc()).offset(skip).limit(limit).all()
    return data_points


@router.get("/stats", response_model=dict)
async def get_statistics(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get statistical summary of data"""
    from sqlalchemy import func
    
    stats = db.query(
        func.count(DataPoint.id).label("total_count"),
        func.avg(DataPoint.value).label("average_value"),
        func.min(DataPoint.value).label("min_value"),
        func.max(DataPoint.value).label("max_value")
    ).first()
    
    return {
        "total_count": stats.total_count or 0,
        "average_value": float(stats.average_value) if stats.average_value else 0.0,
        "min_value": float(stats.min_value) if stats.min_value else 0.0,
        "max_value": float(stats.max_value) if stats.max_value else 0.0
    }
