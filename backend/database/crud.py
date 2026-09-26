from sqlalchemy.orm import Session
from . import models

# 1. Naya alert database mein save karne ke liye function
def create_alert(db: Session, sensor_id: str, risk_level: str, description: str):
    db_alert = models.Alert(
        sensor_id=sensor_id,
        risk_level=risk_level,
        status="New",
        description=description
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

# 2. Saare alerts database se nikalne ke liye function
def get_all_alerts(db: Session):
    return db.query(models.Alert).all()

# 3. Alert ka lifecycle status update karne ke liye function (Step 8 ke liye)
def update_alert_status(db: Session, alert_id: int, new_status: str):
    db_alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if db_alert:
        db_alert.status = new_status
        db.commit()
        db.refresh(db_alert)
    return db_alert