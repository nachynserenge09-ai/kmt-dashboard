from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Разрешаем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/user-status")
async def get_user_status(telegram_id: int = None):
    # Здесь в будущем будет подключение к базе данных (PostgreSQL / SQLite), 
    # где по telegram_id мы будем доставать реальные оценки, курс и группу студента КМТ.
    
    # Для примера возвращаем динамические данные
    return {
        "status": "connected",
        "college": "КМТ им. Бардина",
        "course": 1,  # Твой реальный курс
        "gpa": 4.1,   # Динамический показатель
        "message": "Бэкенд успешно работает для всего КМТ!"
    }

@app.get("/", response_class=HTMLResponse)
async def read_index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Файл index.html не найден на сервере!</h3>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)