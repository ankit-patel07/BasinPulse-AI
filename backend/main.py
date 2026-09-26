from backend.database import connection, models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Saare API modules ko import karna
from backend.api import alerts, map_layers, risk
from backend.simulator import simulator_controller
from backend.websocket import realtime

# Server start hote hi database tables generate karna
models.Base.metadata.create_all(bind=connection.engine)

app = FastAPI(title="Flood & Risk Simulation Alert System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Har ek group ko dashboard par register karna (Yahi missing tha)
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(map_layers.router, prefix="/api/gis", tags=["GIS Map Layers"])
app.include_router(risk.router, prefix="/api/risk", tags=["ML Risk Assessment Engine"])
app.include_router(simulator_controller.router, prefix="/api/simulation", tags=["Sensor Simulation"])

app.include_router(realtime.router,tags=["Realtime WebSocket Stream"])

@app.get("/")
def read_root():
    return {
        "status": "Success", 
        "message": "Backend API is running successfully!"
    }