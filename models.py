from enum import unique
from flask_sqlalchemy import SQLAlchemy
import json
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    nameuser = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    favoritos = db.relationship('Favorito', cascade="all, delete", backref="user")

    def serialize(self):
        return{
            "iduser": self.iduser,
            "name": self.name,
            "last_name": self.last_name,
            "nameuser": self.nameuser
        }

    def serialize_whit_favorito(self):
        return{
            "iduser": self.iduser,
            "name": self.name,
            "nameuser": self.nameuser,
            "last_name": self.last_name,
            "favoritos": self.get_favoritos()
        }

    def get_favoritos(self):
        return list(map(lambda favorito:favorito.serialize(),self.favoritos))    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favorito(db.Model):
    __tablename__='favorito'
    idfavorito = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('user.iduser', ondelete='CASCADE'), nullable=False)
    name_favorito = db.Column(db.String(100))
    
    def serialize(self):
        result=[]
        valor = {
            "name_favorito": self.name_favorito  
        }

        for v in valor.values():
            result.append(v)

        return result[0]

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Personaje(db.Model):
    __tablename__='personaje'
    idpersonaje = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    height= db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(50))

    def serialize(self):
        return{
            "id": self.idpersonaje,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planeta(db.Model):
    __tablename__='planeta'
    idplaneta = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))

    def serialize(self):
        return {
            "id":self.idplaneta,
            "name":self.name,
            "diameter":self.diameter,
            "rotation_period":self.rotation_period,
            "orbital_period":self.orbital_period,
            "gravity":self.gravity,
            "population":self.population,
            "climate":self.climate
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Nave(db.Model):
    __tablename__='nave'
    idnave = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    model = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(50))
    cargo_capacity = db.Column(db.Integer)
    passenger = db.Column(db.Integer)

    def serialize(self):
        return {
            "id":self.idnave,
            "name":self.name,
            "model":self.model,
            "vehicle_class":self.vehicle_class,
            "cargo_capacity":self.cargo_capacity,
            "passenger":self.passenger
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()