from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name: str
    specialization: str

class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str
    medical_history: str | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    medical_history: str | None = None

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    date: str
    time: str
    doctor_id: int
    user_id: int

class AppointmentResponse(BaseModel):
    id: int
    date: str
    time: str
    doctor_id: int
    user_id: int

    class Config:
        orm_mode = True

