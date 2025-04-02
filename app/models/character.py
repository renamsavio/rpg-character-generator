from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Enum as SQLAlchemyEnum

Base = declarative_base()

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
    race_id = Column(Integer, ForeignKey('races.id'))
    class_id = Column(Integer, ForeignKey('character_classes.id'))
    level = Column(Integer)
    attributes = Column(JSON)
    background = Column(String)
    personality_traits = Column(JSON)

    # Relacionamentos (opcional, se você quiser acessar os dados relacionados)
    race = relationship("RaceDB", back_populates="characters")
    character_class = relationship("CharacterClassDB", back_populates="characters")

class Character(BaseModel):
    id: Optional[int] = None
    name: str
    race: str
    character_class: str
    level: int
    attributes: Attributes
    background: str
    personality_traits: List[str]

    class Config:
        from_attributes = True  # Permite que o Pydantic converta o modelo SQLAlchemy em um modelo Pydantic


class CharacterResponse(BaseModel):
    id: Optional[int] = None
    name: str
    race: object
    character_class: object
    level: int
    attributes: Attributes
    background: str
    personality_traits: List[str]

    class Config:
        from_attributes = True  # Permite que o Pydantic converta o modelo SQLAlchemy em um modelo Pydantic
    
    @classmethod
    def from_orm(cls, obj):
        instance = super().from_orm(obj)
        instance.race = obj.race.name if obj.race else None
        instance.character_class = obj.character_class.name if obj.character_class else None
        return instance

class RaceDB(Base):
    __tablename__ = "races"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relacionamento com CharacterDB
    characters = relationship("CharacterDB", back_populates="race")

    class Config:
        from_attributes = True

class CharacterClassDB(Base):
    __tablename__ = "character_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    
    # Relacionamento com CharacterDB
    characters = relationship("CharacterDB", back_populates="character_class")
    class Config:
        from_attributes = True

class CharacterUpdate(BaseModel):
    name: Optional[str] = None               
    race: object = None               
    class_type: Optional[str] = None         
    level: Optional[int] = None              
    attributes: Optional[dict] = None        
    background: Optional[str] = None         
    personality_traits: Optional[List[str]] = None
    
    class Config:
        from_attributes = True
        
        @classmethod
        
        def from_orm(cls, obj):
        
            instance = super().from_orm(obj)
        
            instance.race = obj.race.name if obj.race else None
        
            instance.character_class = obj.character_class.name if obj.character_class else None
    
            return instance