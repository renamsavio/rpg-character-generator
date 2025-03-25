from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.services.character_service import CharacterService
from app.models.character import Character as CharacterModel, CharacterDB, Character, CharacterResponse
from typing import Optional, List
from app.core.database import SessionLocal
#from app.core.database import get_db

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/characters", response_model=CharacterResponse)
async def create_character(character: Character, db: Session = Depends(get_db)):
    """Gera um novo personagem com características a partir do JSON recebido"""
    new_character = CharacterService.create_character(character, db)
    return CharacterResponse.from_orm(new_character)

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