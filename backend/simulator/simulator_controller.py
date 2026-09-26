from fastapi import APIRouter
import random

router = APIRouter()

# API: Live simulation dashboard ke liye realtime data status fetch karna
@router.get("/status")
def get_simulation_status():
    return {
        "simulation_running": True,
        "current_feeds": {
            "rainfall_mm": round(random.uniform(10.0, 150.0), 2),
            "soil_moisture_percentage": round(random.uniform(20.0, 95.0), 2),
            "river_level_meters": round(random.uniform(1.5, 8.0), 2)
        }
    }