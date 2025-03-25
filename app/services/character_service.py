from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.character import CharacterDB, RaceDB, CharacterClassDB, Character
from app.core.database import SessionLocal, engine, Base

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

class CharacterService:
    
    @staticmethod
    def generate_character(character_data: dict, db: Session) -> CharacterDB:
        # Cria um novo personagem a partir dos dados recebidos
        character = CharacterDB(
            name=character_data["name"],
            race=Race(character_data["race"]),
            character_class=CharacterClass(character_data["character_class"]),
            level=character_data["level"],
            attributes={
                "strength": character_data["attributes"]["strength"],
                "dexterity": character_data["attributes"]["dexterity"],
                "constitution": character_data["attributes"]["constitution"],
                "intelligence": character_data["attributes"]["intelligence"],
                "wisdom": character_data["attributes"]["wisdom"],
                "charisma": character_data["attributes"]["charisma"],
            },
            background=character_data["background"],
            personality_traits=character_data["personality_traits"]
        )

        db.add(character)
        db.commit()
        db.refresh(character)
        return character

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