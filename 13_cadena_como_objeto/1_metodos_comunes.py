#################################
##            count            ##
#################################
s = "Estoy aprendiendo a programar en Python"
c = s.lower().count("pytHoN".lower())
# print(c)




















#################################
##         find,rfind          ##
#################################
s = "Python: Estoy aprendiendo a programar en Python. Python es el mejor para empezar"
# print(s.find("Python"))
# print(s.rfind("Python"))










#################################
##         index,rindex        ##
#################################
s = "Estoy aprendiendo a programar en Python .Python  es el mejor para empezar"
print(s.index("Python"))
print(s.rindex("Python"))











#################################
##            join             ##
#################################
l_1 = ["Matemática","Alumno 001",15]
l_2 = ["Biología","Alumno 001",13]
l_3 = ["Historia","Alumno 002",17]
#"Matemática;Alumno 001;15"

s = " | ".join([str(e) for e in l_3])
print(s)















#################################
##          replace            ##
#################################
s = "Estoy aprendiendo a programar en Python"
s_new = s.replace(" ","|")
print(s_new)




















#################################
##            split            ##
#################################
#Número de factura,identificador de empresa,monto,impuesto,cantidad de items
s = "F001-00001223|20012120223|50.21|12.32|5"

l = s.split("|")
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])












s = "F001-00001223|20012120223|50.21|12.32|5\nF001-00001224|20012120223|100|23.32|6\nF001-00001225|20012120223|150.21|36|3"