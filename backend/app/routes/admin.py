from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Doctor
from app.schemas import DoctorCreate, DoctorResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register-doctor", response_model=DoctorResponse)
def register_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = Doctor(name=doctor.name, specialization=doctor.specialization)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor
