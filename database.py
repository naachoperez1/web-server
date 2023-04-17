import sqlite3

def add_entry(conexion,name, email,password):
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?);", (name,email,password))


def get_entries(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()
    return usuarios