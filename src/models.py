from sqlalchemy import Column, Integer, String, DateTime, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = relationship("Favorite", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "favorites": self.favorites
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    user = relationship("User", back_populates="favorites")
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
        }   

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(20))
    skin_color = db.Column(db.String(20))
    eyes_color = db.Column(db.String(20))
    birth_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    homeworld = db.Column(db.String(250))
    url = db.Column(db.String(250))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    starship_ids = db.Column(ARRAY(db.Integer))
    vehicle_ids = db.Column(ARRAY(db.Integer))

    species = relationship("Species", back_populates="characters")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eyes_color': self.eyes_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S') if self.created else None,
            'edited': self.edited.strftime('%Y-%m-%d %H:%M:%S') if self.edited else None,
            'homeworld': self.homeworld,
            'url': self.url
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(20))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(20))
    terrain = db.Column(db.String(20))
    surface_water = db.Column(db.String)
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'diameter': self.diameter,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'gravity': self.gravity,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S') if self.created else None,
            'edited': self.edited.strftime('%Y-%m-%d %H:%M:%S') if self.edited else None,
            'url': self.url
        }
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String)
    manufacturer = db.Column(db.String)
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.DECIMAL(20, 1))
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumable = db.Column(db.String(20))
    films = db.Column(ARRAY(db.String))
    pilots = db.Column(ARRAY(db.String))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': str(self.length),
            'crew': self.crew,
            'passengers': self.passengers,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'cargo_capacity': self.cargo_capacity,
            'consumable': self.consumable,
            'films': self.films,
            'pilots': self.pilots,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S') if self.created else None,
            'edited': self.edited.strftime('%Y-%m-%d %H:%M:%S') if self.edited else None,
            'url': self.url
        }

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    classification = db.Column(db.String(250))
    designation = db.Column(db.String(250))
    average_height = db.Column(db.String(20))
    skin_colors = db.Column(db.String(250))
    hair_colors = db.Column(db.String(250))
    eye_colors = db.Column(db.String(250))
    average_lifespan = db.Column(db.String(20))
    homeworld = db.Column(db.String(250))
    language = db.Column(db.String(250))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    url = db.Column(db.String(250))

    characters = relationship("Character", back_populates="species")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'skin_colors': self.skin_colors,
            'hair_colors': self.hair_colors,
            'eye_colors': self.eye_colors,
            'average_lifespan': self.average_lifespan,
            'homeworld': self.homeworld,
            'language': self.language,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S') if self.created else None,
            'edited': self.edited.strftime('%Y-%m-%d %H:%M:%S') if self.edited else None,
            'url': self.url
        }