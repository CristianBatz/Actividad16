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
        self.prestado = False
        self.prestado_a = None

    def mostrar_info(self, usuarios=None):
        if self.prestado:
            if usuarios and self.prestado_a in usuarios.usuarios:
                nombre_usuario = usuarios.usuarios[self.prestado_a].nombre
                estado = f"Prestado a: {nombre_usuario} (Carnet: {self.prestado_a})"
            else:
                estado = f"Prestado a: {self.prestado_a}"
        else:
            estado = "Disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, Fecha: {self.fecha}, Código: {self.codigo}, Estado: {estado}"


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
        self.usuarios[carnet] = Usuario(nombre, carnet, carrera)

    def mostrar_info(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
        else:
            print("\n Lista de usuarios:")
            for usuario in self.usuarios.values():
                print(usuario.mostrar_info())


class ManipulacionLibros:
    def __init__(self):
        self.libros = {}

    def agregar(self):
        codigo = input("Codigo unico del libro: ")
        if codigo in self.libros:
            print("Ese libro ya esta registrado.")
            return
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        fecha = input("Fecha de publicacion del libro: ")
        self.libros[codigo] = Libro(titulo, autor, fecha, codigo)

    def mostrar_info(self, usuarios=None):
        if not self.libros:
            print("No hay libros registrados")
        else:
            print("\nLista de libros:")
            for libro in self.libros.values():
                print(libro.mostrar_info(usuarios))


class PrestamoDevolucion:
    def __init__(self, manipulacion_libros, manipulacion_usuarios):
        self.manipulacion_libros = manipulacion_libros
        self.manipulacion_usuarios = manipulacion_usuarios

    def prestamo(self, codigo):
        if codigo not in self.manipulacion_libros.libros:
            print("No se encontró el libro.")
            return
        libro = self.manipulacion_libros.libros[codigo]

        if libro.prestado:
            print("Ese libro ya está prestado.")
        else:
            carnet = input("Ingrese el carnet del usuario: ")
            if carnet not in self.manipulacion_usuarios.usuarios:
                print("Usuario no registrado.")
                return
            libro.prestado = True
            libro.prestado_a = carnet
            print(f"Se ha prestado el libro '{libro.titulo}'.")

    def devolucion(self, codigo):
        if codigo not in self.manipulacion_libros.libros:
            print("No se encontró el libro.")
            return
        libro = self.manipulacion_libros.libros[codigo]
        if not libro.prestado:
            print("Ese libro no estaba prestado.")
        else:
            print(f"Se ha devuelto el libro '{libro.titulo}'.")
            libro.prestado = False
            libro.prestado_a = None


registro = ManipulacionUsuario()
registro2 = ManipulacionLibros()
registro3 = PrestamoDevolucion(registro2, registro)
opcion = 0
while opcion != 7:
    print("=== MENU BIBLIOTECA ===")
    print("1. Agregar Usuario")
    print("2. Agregar Libro")
    print("3. Mostrar usuarios")
    print("4. Mostrar libros")
    print("5. Prestamos")
    print("6. Devolver libro")
    print("7. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue
    match opcion:
        case 1:
            registro.agregar()
        case 2:
            registro2.agregar()
        case 3:
            registro.mostrar_info()
        case 4:
            registro2.mostrar_info(registro)
        case 5:
            codigo = input("Ingrese el código del libro a prestar: ")
            registro3.prestamo(codigo)
        case 6:
            codigo = input("Ingrese el código del libro a devolver: ")
            registro3.devolucion(codigo)
