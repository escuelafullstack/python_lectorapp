#Funciones lambda o anónimas
#lambda <argumentos>:<function>
pi = 3.14

def areaCirculo(r):
    return pi*r**2

a_circulo = lambda r:pi*r**2

print(areaCirculo(5))
print(a_circulo(5))


# def calculo(b,h):
#     return b*h/2

# area_triangulo = lambda b,h:calculo(b,h)

# print(area_triangulo(7,5))