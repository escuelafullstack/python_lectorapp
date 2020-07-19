
#Definiendo una excepción


class NuevoTipoError(Exception):
    pass

# raise NuevoTipoError("Esto es un error")

#Ejemplo: Validar un rango de edad 14 y 18 años

class FueraderangoEdadError(Exception):
    def __init__(self,edad,message="Fuera de rango de edad: solo permite entre 14 y 15 años"):
        self.edad = edad
        self.message = message
        super(FueraderangoEdadError,self).__init__(message)

    def __str__(self):
        return "{} años -> {}".format(self.edad,self.message)

edad = 16
if edad < 14 or edad > 18:
    raise FueraderangoEdadError(edad)