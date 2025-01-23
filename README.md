Шаги для запуска проекта:
Убедитесь, что виртуальное окружение активно. В командной строке должно отображаться что-то вроде:


(.venv) PS D:\Programs\VSCode Projects\ehealth-system\backend>
Если оно не активно, активируйте виртуальное окружение:

Windows:
.venv\Scripts\activate
Linux/macOS:
source .venv/bin/activate

Запустите приложение с помощью Uvicorn. Выполните следующую команду в папке backend: uvicorn main:app --reload
Перейдите по адресу http://127.0.0.1:8000 в браузере, чтобы увидеть ваше приложение.


Проверьте Swagger-документацию. FastAPI автоматически генерирует документацию для вашего API. Перейдите по адресу:

http://127.0.0.1:8000/docs для Swagger UI.
http://127.0.0.1:8000/redoc для ReDoc.

