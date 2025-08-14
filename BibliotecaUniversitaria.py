class Usuario:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, carnet: {self.carnet}, carrera: {self.carrera}"


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
        self.usuarios = {}

    def agregar(self):
        carnet = input("Carnet del usuario: ")
        if carnet in self.usuarios:
            print("Ese carnet ya está registrado.")
            return
        nombre = input("Nombre del usuario: ")
        carrera = input("Carrera del usuario: ")
        self.usuarios[carnet]= {
            "nombre": nombre,
            "carrera": carrera
        }

    def mostrar_info(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
        else:
            print("\n Lista de usuarios:")
            for carnet, datos in self.usuarios.items():
                print(f"Carnet: {carnet}, Nombre: {datos['nombre']}, Carrera: {datos['carrera']}")
            print()


class ManipulacionLibros:
    def __init__(self):
        self.libros = {}

    def agregar(self):
        codigo = input("Codigo unico del libro: ")
        if codigo in self.libros:
            print("Ese libro ya registrado.")
            return
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        fecha = input("Fecha de publicacion del libro: ")
        self.libros[codigo] = {
            "titulo": titulo,
            "autor": autor,
            "fecha": fecha,
            "prestado": False
        }


    def mostrar_info(self):
        if not self.libros:
            print("No hay libros registrados")
        else:
            print("\n Lista de libros:")
            for codigo, datos in self.libros.items():
                estado = "Prestado" if datos["prestado"] else "Disponible"
                print(f"Código: {codigo}, Título: {datos['titulo']},"
                    f" Autor: {datos['autor']}, Fecha: {datos['fecha']}, Estado: {estado}")


class PrestamoDevolucion:
    def __init__(self,manipulacion_libros):
        self.manipulacion_libros = manipulacion_libros

    def agregar(self,codigo):
        if codigo not in self.manipulacion_libros.libros:
            print("No se encontró el libro.")
            return
        if self.manipulacion_libros.libros[codigo]["prestado"]:
            print("Ese libro ya está prestado.")
        else:
            self.manipulacion_libros.libros[codigo]["prestado"] = True
            print(f"Se ha prestado el libro "
                  f"'{self.manipulacion_libros.libros[codigo]['titulo']}'.")

    def prestamo(self, codigo):
        if codigo not in self.manipulacion_libros.libros:
            print("No se encontró el libro.")
            return
        if self.manipulacion_libros.libros[codigo]["prestado"]:
            print("Ese libro ya está prestado.")
        else:
            self.manipulacion_libros.libros[codigo]["prestado"] = True
            print(f"Se ha prestado el libro "
                  f"'{self.manipulacion_libros.libros[codigo]['titulo']}'.")


registro = ManipulacionUsuario()
registro2 = ManipulacionLibros()
registro3 = PrestamoDevolucion(registro2)
opcion = 0
while opcion != 4:
    print("=== MENU BIBLIOTECA ===")
    print("1. Agregar Usuario")
    print("2. Agregar Libro")
    print("3. Prestamos y devoluciones")
    print("4. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue
    match opcion:
        case 1:
            registro.agregar()
            registro.mostrar_info()
        case 2:
            registro2.agregar()
