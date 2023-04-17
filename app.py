from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash
from model import db, Usuario
import database
import sqlite3
import threading

app = Flask(__name__)

conexion = conn = sqlite3.connect("YOUR_DATABSE_LOCATION", check_same_thread=False)

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
        database.add_entry(conexion,nombre, correo_electronico, contrasena)
        return inicio()

    elif request.method == 'GET':
        return usuarios()

    conexion.close()
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
