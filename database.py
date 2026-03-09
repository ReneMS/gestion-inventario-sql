import sqlite3

def conectar():
    """Establece conexión con la base de datos."""
    return sqlite3.connect("inventario.db")

def inicializar_db():
    conexion = conectar()
    cursor = conexion.cursor()
    
    # SQL puro para crear la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT,
            stock INTEGER DEFAULT 0,
            precio INTEGER NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("✅ Base de datos relacional inicializada.")

def insertar_producto(nombre, categoria, stock, precio):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Usamos parámetros '?' para evitar SQL Injection (Seguridad)
    query = "INSERT INTO productos (nombre, categoria, stock, precio) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (nombre, categoria, stock, precio))
    
    conexion.commit()
    conexion.close()
    
def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    
    # SQL para traer todo ordenado por nombre
    cursor.execute("SELECT id, nombre, categoria, stock, precio FROM productos ORDER BY nombre ASC")
    datos = cursor.fetchall()
    
    conexion.close()
    return datos