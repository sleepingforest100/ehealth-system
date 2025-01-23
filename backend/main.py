from fastapi import FastAPI
from app.routes import admin, doctor, user
from app.database import Base, engine
from app.routes import appointment


# Создание таблиц
Base.metadata.create_all(bind=engine)

# Инициализация FastAPI
app = FastAPI()

# Подключение маршрутов
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(doctor.router, prefix="/doctor", tags=["Doctor"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])

