from flask_sqlalchemy import SQLAlchemy
import psycopg2
db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo_electronico = db.Column(db.String(100), unique=True)
    contrasena = db.Column(db.String(100))