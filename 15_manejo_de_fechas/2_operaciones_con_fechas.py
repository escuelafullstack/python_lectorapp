from datetime import datetime,timedelta

libros = [['Cáculo I',datetime(2020,1,12)],
          ['Literatura Española',datetime(2020,6,4)],
          ['Musica',datetime(2020,6,7)],
          ['Programación con Python',datetime(2020,7,15)],
          ['Arquitectura',datetime(2020,7,14)],
          ['Infraestructura de AWS',datetime(2020,7,19)]]


#Filtrar todos los libros creados hoy
d_hoy= datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
# print(d_hoy)
libros_creados_hoy = filter(lambda r:r[1] < d_hoy,libros)
# print(list(libros_creados_hoy))




#Filtrar los libros creados en los ultimos 7 días

d_ultimos_7 = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=7)

# print(d_ultimos_7)
libros_creados_ultimos7dias = filter(lambda r:r[1] < d_ultimos_7,libros)
# print(list(libros_creados_ultimos7dias))



#Filtrar los libros creados el mes pasado
d_mes_pasado = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=30)
d_mes_pasado_sup = datetime.now().replace(day=1,hour=0,minute=0,second=0,microsecond=0)
d_mes_pasado_inf = d_mes_pasado.replace(day=1)

libros_creados_mes_pasado = filter(lambda r:r[1] >= d_mes_pasado_inf and r[1] < d_mes_pasado_sup,libros)

print(list(libros_creados_mes_pasado))