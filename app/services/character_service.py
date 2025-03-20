from sqlalchemy.orm import Session
from app.models.character import CharacterDB, Race, CharacterClass, Attributes
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