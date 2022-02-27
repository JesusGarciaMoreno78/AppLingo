import os

from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    password = db.Column(db.String())
    dni = db.Column(db.String(10),nullable=False,unique=True)
    nombre = db.Column(db.String(20),nullable=False)
    apellidos = db.Column(db.String(50),nullable=False)
    telefono = db.Column(db.String(50),nullable=False)
    telefonoAlternativo = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    direccion = db.Column(db.String(50),nullable=False)
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise

    def update(self):
        try:
            db.session.commit()
        except:
            raise

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()


    def set_password(self, password):
        # self.login = generate_password_hash(login, method='pbkdf2:sha512')
        method = "pbkdf2:sha256:260000"
        # method = "plain"
        # method = "pbkdf2:sha512:1000000"
        self.password = generate_password_hash(password,method=method) #Por defecto sha256
        # self.login = login.split("$", 1)[1]


    def check_password(self, password):
        # passHash = 'pbkdf2:sha256:260000$' + self.login
        return check_password_hash(self.password, password)
