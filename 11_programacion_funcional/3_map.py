#Función map
# def al_cuadrado(x):
#     return x*x

pi = 3.14

a_circulo = lambda r:pi*r**2
l = [1,2,3,4,5,6,7,8,9]
res = map(a_circulo,l)
print(list(res))


# l = [1,2,3,4,5,6,7,8,9]
# l_result = list(map(al_cuadrado,l))
# print(l_result)

#[1, 4, 9, 16, 25, 36, 49, 64, 81]
# for i in map(al_cuadrado,l):
#     print(i)