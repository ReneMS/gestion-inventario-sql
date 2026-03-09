# Sistema de Gestión de Inventario SQL 📦🍎

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Una aplicación de consola diseñada para la administración de productos y stock, integrando **Python** con una base de datos relacional **SQLite**. Ideal para la gestión de pequeños inventarios de forma eficiente y segura.

## ✨ Funcionalidades

- **Persistencia Relacional:** Uso de base de datos SQL para almacenar productos de forma permanente.
- **Operaciones CRUD:** Capacidad para insertar nuevos productos y consultar el estado del inventario en tiempo real.
- **Interfaz Limpia:** Menú interactivo por consola con tablas formateadas para una lectura fácil.
- **Seguridad:** Implementación de consultas parametrizadas para prevenir ataques de inyección SQL.

## 📁 Estructura del Proyecto

```text
gestion-inventario-sql/
├── inventario.db    # Archivo de base de datos SQL (generado automáticamente)
├── database.py      # Capa de datos: funciones de conexión y consultas SQL
├── main.py          # Capa de aplicación: menú interactivo y lógica de negocio
└── README.md        # Documentación del proyecto
```

## 🔧 Tecnologías

- **Python 3.14+**
- **SQLite3:** Motor de base de datos ligero y robusto.
- **SQL (DML/DDL):** Creación de tablas, inserción de datos (`INSERT`) y consultas (`SELECT`).

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**

```bash
git clone https://github.com/ReneMS/gestion-inventario-sql.git
cd gestion-inventario-sql
```

2. **Ejecutar la aplicación:**

```bash
python main.py
```

> **Nota:** No requiere instalar librerías externas, ya que SQLite viene integrado en Python.

---

Desarrollado con precisión técnica por [ReneMS](https://github.com/ReneMS)

