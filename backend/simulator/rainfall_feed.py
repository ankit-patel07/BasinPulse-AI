# backend/simulator/rainfall_feed.py
import random
from datetime import datetime

def generate_simulated_rainfall(intensity_mode: str = "normal"):
    """
    Simulation mode ke basis par raw metrics calculations return karna.
    Modes: normal, heavy_monsoon, flash_flood
    """
    if intensity_mode == "flash_flood":
        val = random.uniform(95.0, 160.0)
    elif intensity_mode == "heavy_monsoon":
        val = random.uniform(50.0, 94.0)
    else:
        val = random.uniform(5.0, 49.9)
        
    return {
        "sensor_type": "rainfall_gauge",
        "value_mm": round(val, 2),
        "timestamp": datetime.utcnow().isoformat()
    }