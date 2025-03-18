from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.services.character_service import CharacterService
from app.models.character import Character as CharacterModel, CharacterDB, Race, CharacterClass
from typing import Optional, List
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/characters", response_model=CharacterModel)
async def create_character(character: CharacterModel, db: Session = Depends(get_db)):
    """Gera um novo personagem com características a partir do JSON recebido"""
    character_data = character.dict()  # Converte o modelo Pydantic para um dicionário
    return CharacterService.generate_character(character_data, db)

@router.get("/characters", response_model=List[CharacterModel])
async def list_characters(db: Session = Depends(get_db)):
    """Lista todos os personagens criados"""
    try:
        characters = CharacterService.get_characters(db)
        return characters
    except Exception as e:
        print(f"Erro ao listar personagens: {e}")
        return {"error": "Erro ao listar personagens"}

@router.get("/races", response_model=List[str])
async def list_races():
    """Lista todas as raças disponíveis"""
    return [race.value for race in Race]

@router.get("/classes", response_model=List[str])
async def list_classes():
    """Lista todas as classes disponíveis"""
    return [class_.value for class_ in CharacterClass]