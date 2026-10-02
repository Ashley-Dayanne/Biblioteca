from ZODB import DB, FileStorage
import transaction

from modelos import Autor, Libro


ARCHIVO_BD = "biblioteca.fs"

storage = FileStorage.FileStorage(ARCHIVO_BD)
db = DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, "libros"):
    root.libros = {}

if "L01" not in root.libros:
    autor = Autor("A01", "Gabriel García Márquez", "Colombiana")
    libro = Libro(
        "L01",
        "Cien años de soledad",
        autor,
        "Editorial Sudamericana",
        "Novela",
        417,
    )
    root.libros["L01"] = libro
    transaction.commit()
    print("Libro creado y guardado en ZODB.")
else:
    print("El libro ya existe en la base de datos.")

print("\n=== DATOS RECUPERADOS ===")
for libro in root.libros.values():
    print(libro.mostrar_informacion())

# Se cierra la conexión para comprobar que los datos quedan persistentes.
connection.close()
db.close()
storage.close()

print("\nLa conexión se cerró correctamente.")
print("Vuelve a ejecutar este archivo para comprobar que el libro se recupera.")
