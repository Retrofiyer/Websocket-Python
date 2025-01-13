# app/main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.views.chat_view import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Incluye las rutas del chat
app.include_router(router)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/static/index.html")