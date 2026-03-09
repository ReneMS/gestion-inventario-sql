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
    
    # SQL para traer todo ordenado por ID descendente (más reciente primero)
    cursor.execute("SELECT id, nombre, categoria, stock, precio FROM productos ORDER BY id DESC")
    datos = cursor.fetchall()
    
    conexion.close()
    return datos

def actualizar_stock(id_producto, nuevo_stock):
    conexion = conectar()
    cursor = conexion.cursor()
    # La 'U' de CRUD: UPDATE
    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, id_producto))
    conexion.commit()
    conexion.close()

def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    # La 'D' de CRUD: DELETE
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    conexion.close()

def reiniciar_autoincrement():
    """Reinicia el contador de ID solo si la tabla está vacía"""
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Verificar si hay productos
    cursor.execute("SELECT COUNT(*) FROM productos")
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Reiniciar el autoincrement
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='productos'")
        conexion.commit()
        print("✅ Contador de ID reiniciado.")
    else:
        print("⚠️ No se puede reiniciar: aún hay productos en la base de datos.")
    
    conexion.close()