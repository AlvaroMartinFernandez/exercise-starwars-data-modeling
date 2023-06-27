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
    uid = Column(String(250), primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(String(250), primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(String(250), primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    uid = Column(String(250), ForeignKey('peoples.id'))
    Description = Column(String(250), nullable=False)
    __v= Column(Integer)

class PropertiesPeople(Base):
    __tablename__ = 'propertiespeople'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    people_id = Column(String(250), ForeignKey('people.id'))
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


class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    uid = Column(String(250), ForeignKey('vehicles.id'))
    Description = Column(String(250), nullable=False)
    __v= Column(Integer)

class PropertiesVehicle(Base):
    __tablename__ = 'propertiesvehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    vehicle_id = Column(String(250), ForeignKey('vehicle.id'))

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



class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    uid = Column(String(250), ForeignKey('planets.id'))
    Description = Column(String(250), nullable=False)
    __v= Column(Integer)

class PropertiesPlanet(Base):
    __tablename__ = 'propertiesplanet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    vehicle_id = Column(String(250), ForeignKey('planet.id'))

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

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    vehicle_id=Column(String(250), ForeignKey('propertiesvehicle.id'))
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
class Pilots(Base):
    __tablename__ = 'pilots'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    vehicle_id=Column(String(250), ForeignKey('propertiesvehicle.id'))
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


  
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
