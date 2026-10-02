from ZODB import DB, FileStorage
from persistent.mapping import PersistentMapping
import transaction

from modelos import Autor, Libro, Usuario, Prestamo


ARCHIVO_BD = "biblioteca.fs"

storage = FileStorage.FileStorage(ARCHIVO_BD)
db = DB(storage)
connection = db.open()
root = connection.root()

# Estructuras principales de la BDOO.
if not hasattr(root, "autores"):
    root.autores = PersistentMapping()

if not hasattr(root, "libros"):
    root.libros = PersistentMapping()

if not hasattr(root, "usuarios"):
    root.usuarios = PersistentMapping()

if not hasattr(root, "prestamos"):
    root.prestamos = PersistentMapping()


# Se evita duplicar los datos si el programa se ejecuta nuevamente.
if not root.autores:
    root.autores["A01"] = Autor(
        "A01", "Gabriel García Márquez", "Colombiana"
    )
    root.autores["A02"] = Autor(
        "A02", "Jane Austen", "Británica"
    )
    root.autores["A03"] = Autor(
        "A03", "Julio Verne", "Francesa"
    )

if not root.libros:
    root.libros["L01"] = Libro(
        "L01", "Cien años de soledad", root.autores["A01"],
        "Editorial Sudamericana", "Novela", 417
    )
    root.libros["L02"] = Libro(
        "L02", "El amor en los tiempos del cólera", root.autores["A01"],
        "Editorial Oveja Negra", "Novela", 348
    )
    root.libros["L03"] = Libro(
        "L03", "Orgullo y prejuicio", root.autores["A02"],
        "Penguin Classics", "Romance", 432
    )
    root.libros["L04"] = Libro(
        "L04", "Emma", root.autores["A02"],
        "Vintage Classics", "Novela", 474
    )
    root.libros["L05"] = Libro(
        "L05", "Viaje al centro de la Tierra", root.autores["A03"],
        "Le Livre de Poche", "Ciencia ficción", 304
    )

# Relación autor -> libros.
for autor in root.autores.values():
    autor.libros = []

for libro in root.libros.values():
    libro.autor.libros.append(libro)

if not root.usuarios:
    root.usuarios["U01"] = Usuario(
        "U01", "Ashley Rodríguez", "ashley@biblioteca.com"
    )
    root.usuarios["U02"] = Usuario(
        "U02", "María López", "maria@biblioteca.com"
    )
    root.usuarios["U03"] = Usuario(
        "U03", "Carlos Hernández", "carlos@biblioteca.com"
    )

if not root.prestamos:
    prestamo1 = Prestamo(
        "P01", root.libros["L01"], root.usuarios["U01"], "2026-10-02"
    )
    prestamo2 = Prestamo(
        "P02", root.libros["L03"], root.usuarios["U02"], "2026-10-02"
    )

    root.libros["L01"].prestar()
    root.libros["L03"].prestar()

    root.prestamos["P01"] = prestamo1
    root.prestamos["P02"] = prestamo2

    root.usuarios["U01"].prestamos.append(prestamo1)
    root.usuarios["U02"].prestamos.append(prestamo2)

transaction.commit()

print("=== DISEÑO DE LA BDOO ===")
print("Autores:", len(root.autores))
print("Libros:", len(root.libros))
print("Usuarios:", len(root.usuarios))
print("Préstamos:", len(root.prestamos))

print("\n=== LIBROS Y SUS AUTORES ===")
for libro in root.libros.values():
    print(f"{libro.titulo} -> {libro.autor.nombre}")

print("\n=== PRÉSTAMOS ===")
for prestamo in root.prestamos.values():
    estado = "Activo" if prestamo.activo else "Devuelto"
    print(
        f"{prestamo.id_prestamo}: {prestamo.libro.titulo} -> "
        f"{prestamo.usuario.nombre} | {estado}"
    )

connection.close()
db.close()
storage.close()

print("\nDatos guardados correctamente en ZODB.")
