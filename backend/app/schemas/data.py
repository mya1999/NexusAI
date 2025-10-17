from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class DataPointBase(BaseModel):
    """Base data point schema"""
    name: str
    value: float
    category: str
    metadata: Optional[Dict[str, Any]] = None


class DataPointCreate(DataPointBase):
    """Data point creation schema"""
    pass


class DataPointResponse(DataPointBase):
    """Data point response schema"""
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True


class PredictionRequest(BaseModel):
    """ML prediction request schema"""
    features: list[float]


class PredictionResponse(BaseModel):
    """ML prediction response schema"""
    prediction: float
    confidence: Optional[float] = None
    model_version: str
