#1. Error de Sintaxis
if True:
    print("Hola mundo")

#2. Excepciones
try:
    a = 1/0
except Exception as e:
    print(e)

print("Fin")