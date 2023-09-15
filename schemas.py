from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_de_usuario = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Se debe almacenar de manera segura, por ejemplo, usando hash y salting

    def __init__(self, nombre_de_usuario, email, password):
        self.nombre_de_usuario = nombre_de_usuario
        self.email = email
        self.password = password

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    subtitulo = db.Column(db.String(100))
    cuerpo = db.Column(db.Text, nullable=False)
    fecha_de_publicacion = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, titulo, subtitulo, cuerpo, usuario_id):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.cuerpo = cuerpo
        self.usuario_id = usuario_id
