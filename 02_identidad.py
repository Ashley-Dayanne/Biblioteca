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

# libro2 hace referencia al mismo objeto que libro1.
libro2 = libro1

print("=== COMPROBACIÓN DE IDENTIDAD ===")
print("libro1 == libro2:", libro1 == libro2)

print("\n=== PROPIEDADES ANTES DEL CAMBIO ===")
print("Libro 1:", libro1.titulo)
print("Libro 2:", libro2.titulo)

print("\nModificando el título de libro1...")
libro1.titulo = "Cien años de soledad - Edición especial"

print("\n=== PROPIEDADES DESPUÉS DEL CAMBIO ===")
print("Libro 1:", libro1.titulo)
print("Libro 2:", libro2.titulo)

print("\nConclusión:")
print("Ambas variables apuntan al mismo objeto, por eso el cambio realizado mediante")
print("libro1 también se observa mediante libro2.")
