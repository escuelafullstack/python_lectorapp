#Manejo de Fechas
from datetime import datetime

d = datetime(2020,7,1,12,45,10)
print(d)
print(d.hour)
print(d.minute)
print(d.second)

d_ahora = datetime.now()
print(d_ahora)
#UTC

d_utc_ahora = datetime.utcnow()
print(d_utc_ahora)

#strftime()
s = d_ahora.strftime("%H:%M:%S")
print(s)

#isoformat
print(d_ahora.isoformat("|"))

#isoweekday
print(d_ahora.isoweekday())

#isocalendar
print(d_ahora.isocalendar())



