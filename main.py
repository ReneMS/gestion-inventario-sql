from database import inicializar_db, insertar_producto, obtener_productos

def menu():
    inicializar_db()
    
    while True:
        print("\n--- 🍎 SISTEMA DE INVENTARIO ---")
        print("1. Agregar Producto")
        print("2. Ver Inventario")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            cat = input("Categoría: ")
            stock = int(input("Stock: "))
            precio = int(input("Precio: "))
            insertar_producto(nombre, cat, stock, precio)
            print("✔️ Guardado.")
            
        elif opcion == "2":
            productos = obtener_productos()
            print("\n--- INVENTARIO ACTUAL ---")
            print(f"{'ID':<3} | {'Nombre':<15} | {'Stock':<6} | {'Precio':<8}")
            print("-" * 40)
            for p in productos:
                # p[0]=id, p[1]=nombre, p[3]=stock, p[4]=precio
                print(f"{p[0]:<3} | {p[1]:<15} | {p[3]:<6} | ${p[4]:<8}")
                
        elif opcion == "3":
            break

if __name__ == "__main__":
    menu()