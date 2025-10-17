from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime
from ..db.database import Base


class DataPoint(Base):
    """Data point model for real-time data processing"""
    __tablename__ = "data_points"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float)
    category = Column(String, index=True)
    metadata = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
