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

@app.get("/one_minute")
async def one_minute(request: Request):
    return templates.TemplateResponse("one_minute.html", {"request": request})

@app.get("/hot_potato")
async def hot_potato(request: Request):
    return templates.TemplateResponse("hot_potato.html", {"request": request})

@app.get("/role_play")
async def role_play(request: Request):
    return templates.TemplateResponse("role_play.html", {"request": request})