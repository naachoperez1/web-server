from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash
from model import db, Usuario
import database
import sqlite3
import threading

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1011nacho11@localhost:5432/new_db'
# db.init_app(app)
conexion = conn = sqlite3.connect("C:/Users/NoteBook/data.db", check_same_thread=False)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/usuarios')
def usuarios():
    user = database.get_entries(conexion)
    return render_template('usuarios.html', usuarios=user)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo_electronico = request.form['correo_electronico']
        contrasena = generate_password_hash(request.form['contrasena'])

        # usuario = Usuario(nombre=nombre, correo_electronico=correo_electronico, contrasena=contrasena)
        # db.session.add(usuario)
        # db.session.commit()
        database.add_entry(conexion,nombre, correo_electronico, contrasena)
        return inicio()

    elif request.method == 'GET':
        return usuarios()

    conexion.close()
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')