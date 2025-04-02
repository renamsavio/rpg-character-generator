from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.services.character_service import CharacterService
from app.models.character import Character as Character, CharacterResponse
from typing import List
from app.core.database import SessionLocal

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

@router.get("/characters", response_model=List[CharacterResponse])
async def list_characters(db: Session = Depends(get_db)):
    """Lista todos os personagens criados"""
    try:
        characters = CharacterService.get_characters(db)
        return [CharacterResponse.from_orm(character) for character in characters]
    except Exception as e:
        print(f"Erro ao listar personagens: {e}")
        return {"error": "Erro ao listar personagens"}

@router.get("/classes", response_model=List[str])
async def list_class_names(db: Session = Depends(get_db)):
    """Lista todos os nomes das classes disponíveis sem incluir o ID"""
    return CharacterService.get_classes(db)

@router.get("/races", response_model=List[str])
async def list_race_names(db: Session = Depends(get_db)):
    """Lista todos os nomes das raças disponíveis sem incluir o ID"""
    return CharacterService.get_races(db)

@router.delete("/characters/{character_id}", response_model=dict)
async def remove_character(character_id: int, db: Session = Depends(get_db)):
    """Remove um personagem pelo ID"""
    CharacterService.delete_character(character_id, db)
    return {"detail": "Personagem removido com sucesso"}