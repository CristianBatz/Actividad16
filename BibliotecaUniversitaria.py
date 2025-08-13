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
        self.lista_usuarios = []

    def agregar(self):
        nombre = input("Nombre del usuario: ")
        carnet = input("Carnet del usuario: ")
        carrera = input("Carrera del usuario: ")
        self.lista_usuarios.append(Usuario(nombre, carnet, carrera))

    def mostrar_info(self):
        if not self.lista_usuarios:
            print("No hay usuarios registrados")
        else:
            print("\n Lista de usuarios:")
            for i, usuario in enumerate(self.lista_usuarios, start=1):
                print(f"{i}. {usuario.mostrar_info()}")
            print()


class ManipulacionLibros:
    def __init__(self):
        self.lista_libros = []

    def agregar(self):
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        fecha = input("Fecha de publicacion del libro: ")
        codigo = input("Codigo unico del libro: ")
        self.lista_libros.append(Libro(titulo, autor, fecha, codigo))

    def mostrar_info(self):
        if not self.lista_libros:
            print("No hay libros registrados")
        else:
            print("\n Lista de libros:")
            for i, libro in enumerate(self.lista_libros, start=1):
                print(f"{i}. {libro.mostrar_info()}")


class PrestamoDevolucion:
    def __init__(self):
        self.lista_libro = []

    def agregar(self):
        self.lista_libro.append(ManipulacionLibros())

    def mostrar_info(self):
        if not self.lista_libro:
            print("No hay libros registrados")
        else:
            print("\n Lista de libros:")
            for i, libro in enumerate(self.lista_libro, start=1):
                print(f"{i}. {libro.mostrar_info()}")

    def prestamo(self, titulo):
        if not self.lista_libro:
            print("No hay libros registrados")
        else:
            for libro in self.lista_libro:
                if libro.titulo.lower() == titulo.lower():
                    print(f"Se ha prestado el libro {libro.titulo}")
                    return
                else:
                    print(f"El libro {libro.titulo} ya esta prestado")
                    return
            print(f"No se ha encontrado el libro {titulo}")


registro = ManipulacionUsuario()
registro2 = ManipulacionLibros()
registro3 = PrestamoDevolucion()
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
        case 3:
            registro3.agregar()
