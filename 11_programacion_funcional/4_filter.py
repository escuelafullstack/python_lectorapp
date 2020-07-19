#Función Filter
# l = range(100)

# def es_par(x):
#     return not x%2
notas = [{"id":"001","curso":"A","nota":12},
        {"id":"001","curso":"A","nota":13},
        {"id":"001","curso":"A","nota":20},
        {"id":"001","curso":"A","nota":9},
        {"id":"001","curso":"A","nota":11},
        {"id":"001","curso":"A","nota":17},
        {"id":"001","curso":"A","nota":14}]

#Paradigma funcional
l_aprobados = list(filter(lambda r:r["nota"]<=15,notas))
print(l_aprobados)

#Paradigma imperativo
l_des = []
for n in notas:
    if n["nota"]<=15:
        l_des.append(n)
print(l_des)

