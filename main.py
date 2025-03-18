from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import character_routes

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION
)

app.include_router(character_routes.router, prefix="/api/v1", tags=["characters"])

@app.get("/")
async def root():
    return {
        "message": "Bem-vindo ao Gerador de Personagens de RPG!",
        "docs": "/docs"
    }