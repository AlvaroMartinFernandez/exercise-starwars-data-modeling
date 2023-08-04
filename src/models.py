import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DATETIME
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Peoples(Base):
    __tablename__ = 'peoples'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    height=Column(String(250), nullable=False)
    mass=Column(String(250), nullable=False)
    hair_color= Column(String(250), nullable=False)
    skin_color=Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    created=Column(DATETIME, nullable=False)
    edited= Column(DATETIME, nullable=False)
    homeworld=Column(String(250), nullable=False)
    

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    model= Column(String(250), nullable=False)
    vehicle_class=Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    lenght = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    lenght = Column(String(250), nullable=False)
    passengers=Column(DATETIME, nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    created=Column(DATETIME, nullable=False)
    edited= Column(DATETIME, nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    diameter= Column(String(250), nullable=False)
    rotation_period=Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    Population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    created=Column(DATETIME, nullable=False)
    edited= Column(DATETIME, nullable=False)

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)



class ListFavorites(Base):
    __tablename__ = 'listfavorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"), nullable=False)
    peoples_id=Column(Integer, ForeignKey("peoples.id"), nullable=False)
    vehicles_id=Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    planets_id=Column(Integer, ForeignKey("planets.id"), nullable=False)




  
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
