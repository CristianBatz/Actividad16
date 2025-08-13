class Usuario:
    def __init__(self, nombre, carnet,carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, carnet: {self.carnet}, carrera: {self.carrera}")

class Libro:
    def __init__(self, titulo, autor, fecha, codigo):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.codigo = codigo

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Fecha: {self.fecha}")
        print(f"Codigo: {self.codigo}")

class ManipulacionUsuario:
    def __init__(self):
        self.lista_usuarios = []

    def agregar(self):
        nombre = input("Nombre del usuario: ")
        carnet = input("Carnet del usuario: ")
        carrera = input("Carrera del usuario: ")
        self.lista_usuarios.append(Usuario(nombre, carnet, carrera))

class ManipulacionLibros:
    def __init__(self):
        self.lista_libros = []

    def agregar(self):
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        fecha = input("Fecha de publicacion del libro: ")
        codigo = input("Codigo unico del libro: ")
        self.lista_libros.append(Libro(titulo, autor, fecha, codigo))




