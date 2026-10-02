from modelos import Autor, Libro


autor1 = Autor("A01", "Gabriel García Márquez", "Colombiana")

libro1 = Libro(
    "L01",
    "Cien años de soledad",
    autor1,
    editorial="Editorial Sudamericana",
    categoria="Novela",
    numero_paginas=417,
)

print("=== PROPIEDADES DEL LIBRO ===")
print("ID:", libro1.id_libro)
print("Título:", libro1.titulo)
print("Autor:", libro1.autor.nombre)
print("Editorial:", libro1.editorial)
print("Categoría:", libro1.categoria)
print("Número de páginas:", libro1.numero_paginas)

print("\n=== MODIFICACIÓN DE PROPIEDADES ===")
libro1.editorial = "Editorial Diana"
libro1.categoria = "Literatura"
libro1.numero_paginas = 450

print("Editorial:", libro1.editorial)
print("Categoría:", libro1.categoria)
print("Número de páginas:", libro1.numero_paginas)
