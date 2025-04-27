from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static assets
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
# Jinja2 templates directory
templates = Jinja2Templates(directory="backend/templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})