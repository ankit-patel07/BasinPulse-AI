from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .connection import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    risk_level = Column(String)  # High, Medium, Low
    status = Column(String, default="New")  # New -> Acknowledged -> Inspection -> Resolved
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String)  # rainfall, soil_moisture, river_level
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)