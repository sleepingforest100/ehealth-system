from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import Request

# Initialize FastAPI app
app = FastAPI()

# Correct directory path for Jinja2 templates
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "frontend/build")

# Route to serve the index.html
@app.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
