from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash
import database
import sqlite3
import threading

app = Flask(__name__)

# Create connection with database.
conexion = conn = sqlite3.connect("YOUR_DATABSE_LOCATION", check_same_thread=False)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/usuarios')
def usuarios():
    # Function that returns a cursor with all the users in the database.
    user = database.get_entries(conexion)
    return render_template('usuarios.html', usuarios=user) # We pass 'user' as a parameter to the html so it shows it on the web page.

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Get the inputs from the form.
        nombre = request.form['nombre']
        correo_electronico = request.form['correo_electronico']
        contrasena = generate_password_hash(request.form['contrasena'])
        # Add these inputs to the database.
        database.add_entry(conexion,nombre, correo_electronico, contrasena)
        return inicio()

    elif request.method == 'GET':
        return usuarios()

    conexion.close()
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
