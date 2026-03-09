from database import inicializar_db, insertar_producto, obtener_productos, actualizar_stock, eliminar_producto

def menu():
    inicializar_db()
    
    while True:
        print("\n--- 🍎 SISTEMA DE INVENTARIO (CRUD COMPLETO) ---")
        print("1. Agregar Producto (Create)")
        print("2. Ver Inventario (Read)")
        print("3. Actualizar Stock (Update)")
        print("4. Eliminar Producto (Delete)")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                cat = input("Categoría: ")
                stock = int(input("Stock: "))
                precio = int(input("Precio: "))
                insertar_producto(nombre, cat, stock, precio)
                print("✔️ Producto creado.")
            except ValueError:
                print("❌ Error: Stock y Precio deben ser números enteros.")
            
        elif opcion == "2":
            productos = obtener_productos()
            print("\n--- INVENTARIO ACTUAL ---")
            for p in productos:
                print(f"ID: {p[0]} | {p[1]:<15} | Stock: {p[3]:<5} | ${p[4]}")
                
        elif opcion == "3":
            try:
                id_prod = int(input("ID del producto a actualizar: "))
                nuevo_val = int(input("Nuevo stock total: "))
                actualizar_stock(id_prod, nuevo_val)
                print("✔️ Stock actualizado.")
            except ValueError:
                print("❌ Error: ID y Stock deben ser números enteros.")
            
        elif opcion == "4":
            try:
                id_prod = int(input("ID del producto a eliminar: "))
                confirmar = input(f"¿Estás seguro de eliminar el ID {id_prod}? (s/n): ")
                if confirmar.lower() == 's':
                    eliminar_producto(id_prod)
                    print("❌ Producto eliminado.")
            except ValueError:
                print("❌ Error: El ID debe ser un número entero.")
                
        elif opcion == "5":
            break

        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
