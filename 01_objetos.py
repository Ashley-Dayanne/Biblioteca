from modelos import Autor, Libro


def mostrar_informacion(libro):
    print(libro.mostrar_informacion())


autor1 = Autor("A01", "Gabriel García Márquez", "Colombiana")

libro1 = Libro(
    "L01",
    "Cien años de soledad",
    autor1,
    "Editorial Sudamericana",
    "Novela",
    417,
)

libro2 = Libro(
    "L02",
    "El amor en los tiempos del cólera",
    autor1,
    "Editorial Oveja Negra",
    "Novela",
    348,
)

# Tercer libro solicitado en la actividad.
libro3 = Libro(
    "L03",
    "Crónica de una muerte anunciada",
    autor1,
    "Editorial Sudamericana",
    "Novela",
    122,
)

libros = [libro1, libro2, libro3]

print("=== LIBROS DE LA BIBLIOTECA ===")
for libro in libros:
    mostrar_informacion(libro)

print("\n=== ELEMENTOS DEL OBJETO ===")
print("Estado: representa la situación actual del libro, por ejemplo Disponible o Prestado.")
print("Propiedades: son los datos del libro, como id_libro, titulo, autor, editorial y categoria.")
print("Comportamiento: son las acciones que puede realizar el objeto, como prestar(), devolver() y mostrar_informacion().")
