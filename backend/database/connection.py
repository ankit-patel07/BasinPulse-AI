from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Local SQLite database file ka path
DATABASE_URL = "sqlite:///./sensor_simulation.db"

# Engine aur Connection setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database Session ko manage karne ke liye dependency (APIs mein kaam aayegi)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()