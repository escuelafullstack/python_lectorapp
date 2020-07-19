import decimal

#Sentencia de limpieza : with
registros = open("registro.txt","r")
with registros as f:
    for l in f:
        print(l)



with decimal.localcontext() as c:
    c.prec = 2
    print(decimal.getcontext())

print(decimal.getcontext())

