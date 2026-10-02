from ZODB import DB, FileStorage

ARCHIVO_BD = "biblioteca.fs"

storage = FileStorage.FileStorage(ARCHIVO_BD)
db = DB(storage)
connection = db.open()
root = connection.root()


def listar_libros():
    print("\n=== TODOS LOS LIBROS ===")
    for libro in root.libros.values():
        print(libro.mostrar_informacion())


def buscar_libro_por_id(id_libro):
    return root.libros.get(id_libro)


def buscar_libros_por_titulo(texto):
    texto = texto.lower()
    return [
        libro
        for libro in root.libros.values()
        if texto in libro.titulo.lower()
    ]


def buscar_libros_por_categoria(categoria):
    categoria = categoria.lower()
    return [
        libro
        for libro in root.libros.values()
        if libro.categoria.lower() == categoria
    ]


def listar_libros_disponibles():
    return [
        libro for libro in root.libros.values()
        if libro.disponible
    ]


def listar_libros_prestados():
    return [
        libro for libro in root.libros.values()
        if not libro.disponible
    ]


def buscar_libros_por_autor(id_autor):
    return [
        libro for libro in root.libros.values()
        if libro.autor.id_autor == id_autor
    ]


def listar_usuarios():
    print("\n=== USUARIOS ===")
    for usuario in root.usuarios.values():
        print(usuario.mostrar_informacion())


def listar_prestamos_activos():
    print("\n=== PRÉSTAMOS ACTIVOS ===")
    for prestamo in root.prestamos.values():
        if prestamo.activo:
            print(
                f"{prestamo.id_prestamo} | "
                f"Libro: {prestamo.libro.titulo} | "
                f"Usuario: {prestamo.usuario.nombre} | "
                f"Fecha: {prestamo.fecha}"
            )


listar_libros()
listar_usuarios()
listar_prestamos_activos()

print("\n=== BÚSQUEDA POR ID ===")
libro = buscar_libro_por_id("L03")
if libro:
    print(libro.mostrar_informacion())

print("\n=== BÚSQUEDA POR TÍTULO ===")
for libro in buscar_libros_por_titulo("emma"):
    print(libro.mostrar_informacion())

print("\n=== BÚSQUEDA POR CATEGORÍA ===")
for libro in buscar_libros_por_categoria("Novela"):
    print(libro.mostrar_informacion())

print("\n=== LIBROS DISPONIBLES ===")
for libro in listar_libros_disponibles():
    print(libro.mostrar_informacion())

print("\n=== LIBROS PRESTADOS ===")
for libro in listar_libros_prestados():
    print(libro.mostrar_informacion())

print("\n=== LIBROS DE UN AUTOR ===")
for libro in buscar_libros_por_autor("A02"):
    print(libro.mostrar_informacion())


connection.close()
db.close()
storage.close()
