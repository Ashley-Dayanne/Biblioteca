from persistent import Persistent


class Autor(Persistent):
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def mostrar_informacion(self):
        return f"{self.nombre} - {self.nacionalidad}"


class Usuario(Persistent):
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.prestamos = []

    def mostrar_informacion(self):
        return f"{self.nombre} - {self.correo}"


class Libro(Persistent):
    def __init__(
        self,
        id_libro,
        titulo,
        autor,
        editorial="",
        categoria="",
        numero_paginas=0,
    ):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
        self.numero_paginas = numero_paginas
        self.disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return (
            f"{self.id_libro} | {self.titulo} | "
            f"Autor: {self.autor.nombre} | {estado}"
        )

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        self._p_changed = True
        return True

    def devolver(self):
        if self.disponible:
            return False
        self.disponible = True
        self._p_changed = True
        return True


class Prestamo(Persistent):
    def __init__(self, id_prestamo, libro, usuario, fecha):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha
        self.activo = True

    def devolver(self):
        if self.activo:
            self.libro.devolver()
            self.activo = False
            self._p_changed = True
            return True
        return False
