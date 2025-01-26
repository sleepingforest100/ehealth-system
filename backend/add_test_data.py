import sqlite3

connection = sqlite3.connect("ehealth.db")
cursor = connection.cursor()

# Добавление тестовых пользователей
cursor.execute("""
    INSERT INTO users (name, email, medical_history) VALUES
    ('John Doe', 'john@example.com', 'Diabetes'),
    ('Jane Smith', 'jane@example.com', 'Healthy');
""")

# Добавление тестовых докторов
cursor.execute("""
    INSERT INTO doctors (name, specialization) VALUES
    ('Dr. Brown', 'Cardiologist'),
    ('Dr. Green', 'Dermatologist');
""")

connection.commit()
connection.close()
