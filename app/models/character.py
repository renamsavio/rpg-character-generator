from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Enum as SQLAlchemyEnum

Base = declarative_base()

# Definição dos Enums
class Race(str, Enum):
    HUMAN = "Humano"
    ELF = "Elfo"
    DWARF = "Anão"
    HALFLING = "Halfling"
    DRAGONBORN = "Draconato"
    TIEFLING = "Tiefling"
    HALF_ORC = "Meio-Orc"

class CharacterClass(str, Enum):
    WARRIOR = "Guerreiro"
    MAGE = "Mago"
    CLERIC = "Clérigo"
    ROGUE = "Ladino"
    PALADIN = "Paladino"
    RANGER = "Patrulheiro"
    BARD = "Bardo"

class Attributes(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

class CharacterDB(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    race = SQLAlchemyEnum(Race)
    character_class = SQLAlchemyEnum(CharacterClass)
    level = Column(Integer)
    attributes = Column(JSON)  # Certifique-se de que esta coluna está definida
    background = Column(String)
    personality_traits = Column(JSON)

class Character(BaseModel):
    id: Optional[int] = None
    name: str
    race: str  # Usando Enum do SQLAlchemy
    character_class: str 
    level: int
    attributes: Attributes  # Usando a classe Attributes
    background: str
    personality_traits: List[str]  # Mantido como lista de strings

    class Config:
        orm_mode = True  # Permite que o Pydantic converta o modelo SQLAlchemy em um modelo Pydantic