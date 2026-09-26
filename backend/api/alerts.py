from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import crud, connection

router = APIRouter()

# Input check karne ke liye Pydantic schemas
class AlertCreate(BaseModel):
    sensor_id: str
    risk_level: str
    description: str

class StatusUpdate(BaseModel):
    status: str  # New, Acknowledged, Inspection, Resolved

# 1. API: Saare alerts dekhne ke liye
@router.get("/")
def read_alerts(db: Session = Depends(connection.get_db)):
    return crud.get_all_alerts(db)

# 2. API: Naya alert trigger karne ke liye (Simulation engine iska use karega)
@router.post("/trigger")
def trigger_alert(alert: AlertCreate, db: Session = Depends(connection.get_db)):
    return crud.create_alert(db, alert.sensor_id, alert.risk_level, alert.description)

# 3. API: Alert ka workflow status change karne ke liye (Step 8 Workflow)
@router.put("/{alert_id}/status")
def change_alert_status(alert_id: int, status_update: StatusUpdate, db: Session = Depends(connection.get_db)):
    allowed_statuses = ["New", "Acknowledged", "Inspection", "Resolved"]
    if status_update.status not in allowed_statuses:
        raise HTTPException(status_code=400, detail="Invalid status. Must be New, Acknowledged, Inspection, or Resolved.")
    
    updated_alert = crud.update_alert_status(db, alert_id, status_update.status)
    if not updated_alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return updated_alert