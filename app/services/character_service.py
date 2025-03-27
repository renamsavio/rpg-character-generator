from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.character import CharacterDB, RaceDB, CharacterClassDB, Character
from app.core.database import SessionLocal, engine, Base

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

class CharacterService:
    
    @staticmethod
    def get_characters(db: Session) -> list:
        return db.query(CharacterDB).all()

    @staticmethod
    def create_character(character: Character, db: Session) -> CharacterDB:
        # Consultar o ID da raça
        race = db.query(RaceDB).filter(RaceDB.name == character.race).first()
        if race is None:
            raise HTTPException(status_code=400, detail="Raça inválida")

        # Consultar o ID da classe
        character_class = db.query(CharacterClassDB).filter(CharacterClassDB.name == character.character_class).first()
        if character_class is None:
            raise HTTPException(status_code=400, detail="Classe inválida")

        # Criar uma nova instância de CharacterDB
        new_character = CharacterDB(
            name=character.name,
            race_id=race.id,  # Usando o ID da raça obtido da consulta
            class_id=character_class.id,  # Usando o ID da classe obtido da consulta
            level=character.level,
            attributes={
                "strength": character.attributes.strength,
                "dexterity": character.attributes.dexterity,
                "constitution": character.attributes.constitution,
                "intelligence": character.attributes.intelligence,
                "wisdom": character.attributes.wisdom,
                "charisma": character.attributes.charisma,
            },
            background=character.background,
            personality_traits=character.personality_traits
        )

        # Adicionar ao banco de dados
        db.add(new_character)
        db.commit()
        db.refresh(new_character)

        return new_character

    @staticmethod
    def get_races(db: Session) -> list:
        # Consultar todas as raças e retornar apenas os nomes
        return [race.name for race in db.query(RaceDB).all()]
    
    @staticmethod
    def get_classes(db: Session) -> list:
        # Consultar todas as classes e retornar apenas os nomes
        return [classes.name for classes in db.query(CharacterClassDB).all()]
    
    