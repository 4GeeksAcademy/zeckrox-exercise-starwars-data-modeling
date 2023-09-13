import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Date, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    register_date = Column(Date(), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    terrain = Column(String(250))
    climate = Column(String(250), nullable=False)
    diameter = Column(Float, nullable=False)

    
class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    gender = Column(String(20), nullable=False)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    skin_color = Column(String(50), nullable=False)
    birth_year = Column(String(30), nullable=False)

    
class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=False)
    planet = relationship(Planets)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    character = relationship(Characters)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
