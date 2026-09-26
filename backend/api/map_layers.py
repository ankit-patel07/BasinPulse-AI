from fastapi import APIRouter

router = APIRouter()

# API: Frontend map par high-risk zones (Polygons) show karne ke liye data
@router.get("/zones")
def get_flood_zones():
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"zone_name": "Red Zone A", "risk": "High"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [75.0, 30.0], [75.1, 30.0], [75.1, 30.1], [75.0, 30.1], [75.0, 30.0]
                    ]]
                }
            },
            {
                "type": "Feature",
                "properties": {"zone_name": "Yellow Zone B", "risk": "Medium"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [75.2, 30.0], [75.3, 30.0], [75.3, 30.1], [75.2, 30.1], [75.2, 30.0]
                    ]]
                }
            }
        ]
    }