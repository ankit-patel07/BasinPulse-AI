# backend/services/ml_service.py

def predict_flood_risk(rainfall: float, soil_moisture: float, river_level: float):
    """
    Dummy ML engine framework: Jo values ke basis par mathematical threshold compute karta hai.
    """
    # Agar teenon conditions extreme hain, toh critical risk hai
    if river_level > 5.5 or (rainfall > 100.0 and soil_moisture > 85.0):
        return {
            "risk_score": 0.92,
            "risk_level": "High",
            "decision": "Immediate alert dispatch required. Flash flood risk detected."
        }
    elif river_level > 3.5 or rainfall > 60.0:
        return {
            "risk_score": 0.55,
            "risk_level": "Medium",
            "decision": "Water levels rising. Continuous observation recommended."
        }
    else:
        return {
            "risk_score": 0.15,
            "risk_level": "Low",
            "decision": "All parameters normal."
        }