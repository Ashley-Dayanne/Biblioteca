from modelos import Autor, Libro


autor1 = Autor("A01", "Gabriel García Márquez", "Colombiana")

libro1 = Libro(
    "L01",
    "Cien años de soledad",
    autor1,
    "Editorial Sudamericana",
    "Novela",
    417,
)

print("=== PRUEBA DEL COMPORTAMIENTO DEL LIBRO ===")

if libro1.disponible:
    print("Libro disponible.")

if libro1.prestar():
    print("Libro prestado correctamente.")
else:
    print("No fue posible prestar el libro.")

# Segundo intento: debe ser rechazado.
if libro1.prestar():
    print("Libro prestado correctamente.")
else:
    print("El libro no está disponible.")

if libro1.devolver():
    print("Libro devuelto correctamente.")
else:
    print("El libro ya estaba disponible.")

print("\nEstado final:", "Disponible" if libro1.disponible else "Prestado")
