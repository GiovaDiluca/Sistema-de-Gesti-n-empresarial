# app/database/db.py
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "erp.db")


def conectar():
    return sqlite3.connect(DB_PATH)


def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        salario REAL NOT NULL,
        fecha_ingreso TEXT NOT NULL,
        puesto TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nomina (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empleado_id INTEGER,
        mes TEXT,
        salario_bruto REAL,
        deducciones REAL,
        impuestos REAL,
        FOREIGN KEY (empleado_id) REFERENCES empleados(id)
    )
    """)

    conn.commit()
    conn.close()


def agregar_empleado(nombre, apellido, salario, fecha, puesto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO empleados (nombre, apellido, salario, fecha_ingreso, puesto)
    VALUES (?, ?, ?, ?, ?)
    """, (nombre, apellido, salario, fecha, puesto))

    conn.commit()
    conn.close()


def obtener_empleados():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()

    conn.close()
    return empleados

def obtener_nominas_por_empleado(empleado_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, mes, salario_bruto, deducciones, impuestos
    FROM nomina
    WHERE empleado_id = ?
    """, (empleado_id,))

    datos = cursor.fetchall()
    conn.close()
    return datos

