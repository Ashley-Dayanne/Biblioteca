# BibliotecaBDOO

Proyecto de Base de Datos Orientada a Objetos desarrollado con Python y ZODB.

## Estructura

- `modelos.py`: clases persistentes `Autor`, `Libro`, `Usuario` y `Prestamo`.
- `01_objetos.py`: objetos, estado, propiedades y comportamiento.
- `02_identidad.py`: comprobación de identidad de objetos.
- `03_propiedades.py`: propiedades de los libros.
- `04_comportamiento.py`: comportamiento de préstamo y devolución.
- `05_persistencia.py`: conexión y persistencia con ZODB.
- `06_diseno_bdoo.py`: diseño completo con autores, libros, usuarios y préstamos.
- `07_consultas.py`: consultas sobre los objetos almacenados.
- `requirements.txt`: dependencias del proyecto.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución recomendada

Ejecutar primero:

```bash
python 06_diseno_bdoo.py
```

Después:

```bash
python 07_consultas.py
```

Para comprobar la persistencia:

```bash
python 05_persistencia.py
```

El archivo `biblioteca.fs` es creado por ZODB y contiene los datos persistentes.
