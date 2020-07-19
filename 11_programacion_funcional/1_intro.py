
#Las funciones son tratadas como un valor o entidad - 
#Ciudadanos de primera clase

# + - *
def operacion(op):
    def suma(a,b):
        return a+b
    def resta(a,b):
        return a-b
    def producto(a,b):
        return a*b

    operaciones = {
        "+":suma,
        "-":resta,
        "*":producto
    }
    return operaciones[op] # retorna un función

print(operacion("-")(12,15))

# print(operacion("-")(34,12))

#Evita efectos secundarios

var_global = 0 # variable mutable

def suma(a,b):
    var_global = 10 # cambia el valor de la variable
    return a+b


