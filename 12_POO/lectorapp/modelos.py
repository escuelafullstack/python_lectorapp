from datetime import datetime
import pytz
tz_lima  = pytz.timezone("America/Lima")

class Biblioteca:
    def __init__(self,id,nombre,lector=None,libros=None):
        self.id = id
        self.nombre = nombre
        self.lector = lector if lector is not None else "-"
        self.libros = libros if libros is not None else []
        self.__total_libros = len(self.libros)
        
    def obtener_total_libros(self):
        return self.__total_libros
    
    def __cambiar_total_libros(self,valor):
        self.__total_libros = valor

    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return "Biblioteca <{},{}>".format(self.nombre,self.id)

    def __add__(self,obj):
        libros = self.libros + obj.libros
        libros = list(set(libros))
        return Biblioteca(3,"{} - {}".format(self.nombre,obj.nombre),libros=libros)
    
    def append(self,libro):
        pass

    # def __lt__(self, other): Menor que '<'
    #   # return comparison
    # def __le__(self, other): Menor igual que '<='
    #     # return comparison
    # def __eq__(self, other): igual que '=='
    #     # return comparison
    # def __ne__(self, other): no es igual que '!='
    #     # return comparison
    # def __gt__(self, other): mayor que '>'
    #     # return comparison
    # def __ge__(self, other): menor que '>='
    #     # return comparison

    def __lt__(self,obj):
        return len(self.libros) < len(obj.libros)
    
    def __eq__(self,obj):
        return self.id == obj.id

    def agregar_un_libro(self,libro):
        if type(libro) != Libro:
            raise TypeError("Tipo de dato incorrecto: Se ingreso {}, y se requiere {}".format(type(libro),"Libro"))

        self.libros.append(libro)
        self.__cambiar_total_libros(len(self.libros))
        #     print("Se agrego el libro de forma exitosa")
        # else:
        #     print("Solo puede agregar entidades de tipo libro")

class Libro:
    def __init__(self,id,titulo):
        self.id = id
        self.titulo = titulo
        self.date_create = datetime.now(pytz.UTC)

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return "Libro <{},{}>".format(self.titulo,self.id)

class Lector:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.bibliotecas = []

    def __str__(self):
        return self.nombre

    def agregar_biblioteca(self,biblioteca):
        if len(self.bibliotecas)<3:
            self.bibliotecas.append(biblioteca)
        else:
            print("Solo puedes tener hasta 3 bibliotecas")

class LectorBasic(Lector):
    def __init__(self,id,nombre):
        super().__init__(id,nombre)
        self.privado_bibliotecas = []

    def agregar_biblioteca_privada(self,biblioteca):
        if len(self.privado_bibliotecas)<3:
            self.privado_bibliotecas.append(biblioteca)
        else:
            print("Solo puedes tener hasta 3 bibliotecas")
        
class LectorPremium(LectorBasic):
    def agregar_biblioteca_privada(self,biblioteca):
        self.privado_bibliotecas.append(biblioteca)



biblioteca_1 = Biblioteca(1,"Libros de matemática")
biblioteca_2 = Biblioteca(2,"Cuentos")


libro_1 = Libro(1,"Libro de álgebra")
libro_2 = Libro(2,"Libro de aritmética")
libro_3 = Libro(3,"Libro de Geometŕia")
libro_4 = Libro(4,"Cuento 1")
libro_5 = Libro(5,"Cuento 2")
print(libro_1.date_create)
print(libro_1.date_create.astimezone(tz_lima))

biblioteca_1.agregar_un_libro(libro_1)
biblioteca_1.agregar_un_libro(libro_2)

# biblioteca_2.agregar_un_libro(libro_4)
# biblioteca_2.agregar_un_libro(libro_1)
# biblioteca_2.agregar_un_libro(libro_2)
# biblioteca_2.agregar_un_libro(libro_5)

# print(biblioteca_1.libros)
# print(biblioteca_2.libros)

# biblioteca_3 = biblioteca_1+biblioteca_2
# print(biblioteca_3.libros)

# Lector_1 = LectorPremium(1,"Daniel")
# Lector_1.agregar_biblioteca(biblioteca_1)
# Lector_1.agregar_biblioteca_privada(biblioteca_2)
# Lector_1.agregar_biblioteca_privada(biblioteca_1)
# print(Lector_1.privado_bibliotecas)

# print(biblioteca_3==biblioteca_1)

# print(biblioteca_3.obtener_total_libros())
# biblioteca_3.__cambiar_total_libros(4)

# print(biblioteca_3.obtener_total_libros())