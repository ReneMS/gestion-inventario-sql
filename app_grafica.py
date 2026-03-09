import flet as ft
from database import obtener_productos, insertar_producto, inicializar_db, eliminar_producto, reiniciar_autoincrement

def main(page: ft.Page):
    page.title = "Inventario SQL Pro - ReneMS"
    page.window_width = 800 # Un poco más ancho para la nueva columna
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.DARK
    
    inicializar_db()

    # --- ELEMENTOS DE INTERFAZ ---
    txt_nombre = ft.TextField(label="Nombre del Producto", expand=True)
    txt_precio = ft.TextField(label="Precio", width=150, prefix=ft.Text("$"))
    txt_stock = ft.TextField(label="Stock", width=150)
    txt_buscar = ft.TextField(label="Buscar...", prefix_icon=ft.Icons.SEARCH, on_change=lambda e: cargar_datos(e.control.value))

    tabla_productos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Stock")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Acciones")), # Nueva columna
        ],
        rows=[]
    )

    def borrar_click(id_prod, nombre_prod):
        # Función que se ejecuta al presionar el basurero
        eliminar_producto(id_prod)
        page.snack_bar = ft.SnackBar(ft.Text(f"Eliminado: {nombre_prod}"), bgcolor=ft.Colors.RED_ACCENT)
        page.snack_bar.open = True
        cargar_datos() # Refrescar tabla
        
        # Si no quedan productos, reiniciar el contador
        if len(tabla_productos.rows) == 0:
            reiniciar_autoincrement()
            page.update()

    def cargar_datos(filtro=""):
        tabla_productos.rows.clear()
        for p in obtener_productos():
            if filtro.lower() in p[1].lower():
                # Guardamos el ID y nombre para la función de borrar
                id_actual = p[0]
                nombre_actual = p[1]
                
                tabla_productos.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(p[0]))),
                            ft.DataCell(ft.Text(p[1])),
                            ft.DataCell(ft.Text(str(p[3]))),
                            ft.DataCell(ft.Text(f"${p[4]}")),
                            ft.DataCell(
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_FOREVER,
                                    icon_color="red",
                                    on_click=lambda e, id=id_actual, nom=nombre_actual: borrar_click(id, nom)
                                )
                            ),
                        ]
                    )
                )
        page.update()

    def guardar_click(e):
        if txt_nombre.value and txt_precio.value:
            try:
                stock = int(txt_stock.value) if txt_stock.value else 0
                precio = int(txt_precio.value)
                insertar_producto(txt_nombre.value, "General", stock, precio)
                txt_nombre.value = ""; txt_precio.value = ""; txt_stock.value = ""
                cargar_datos()
                page.snack_bar = ft.SnackBar(ft.Text("Producto guardado correctamente"), bgcolor=ft.Colors.GREEN_ACCENT)
                page.snack_bar.open = True
                page.update()
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text("Error: Precio y Stock deben ser números"), bgcolor=ft.Colors.RED_ACCENT)
                page.snack_bar.open = True
                page.update()

    btn_guardar = ft.ElevatedButton("Guardar", icon=ft.Icons.SAVE, on_click=guardar_click)

    # --- DISEÑO ---
    page.add(
        ft.Text("Gestión de Inventario SQL", size=30, weight="bold"),
        ft.Card(ft.Container(padding=20, content=ft.Column([
            ft.Row([txt_nombre]),
            ft.Row([txt_precio, txt_stock, btn_guardar], alignment="end")
        ]))),
        ft.Divider(),
        txt_buscar,
        ft.Column([tabla_productos], scroll="always", expand=True)
    )
    cargar_datos()

ft.app(main)