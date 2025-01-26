from app.database import SessionLocal
from app.models import Admin, Doctor, User, Appointment

# Подключение к базе данных
db = SessionLocal()

# Функция для получения данных из таблицы
def fetch_table_data(model):
    rows = db.query(model).all()
    return rows

# Функция для отображения данных таблицы
def display_data():
    tables = {
        "Admins": Admin,
        "Doctors": Doctor,
        "Users": User,
        "Appointments": Appointment,
    }

    with open("database_content.txt", "w", encoding="utf-8") as file:
        for table_name, model in tables.items():
            file.write(f"\n=== Содержимое таблицы {table_name} ===\n")
            rows = fetch_table_data(model)
            if rows:
                for row in rows:
                    # Преобразуем объект модели в строку с его атрибутами
                    row_data = ', '.join([f"{col}: {getattr(row, col)}" for col in row.__table__.columns.keys()])
                    file.write(f"{row_data}\n")
            else:
                file.write("Таблица пуста.\n")

    print("Данные сохранены в файл 'database_content.txt'.")

# Выполняем просмотр данных
if __name__ == "__main__":
    display_data()
    db.close()
