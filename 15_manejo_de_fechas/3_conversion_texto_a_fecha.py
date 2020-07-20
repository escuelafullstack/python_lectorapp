from datetime import datetime

fecha_1 = "12/7/2020"
fecha_2 = "1-7-2020"
fecha_3 = "06/2020"
fecha_4 = "12072020"
fecha_hora = "01/07/2020 15:00:30 PM"

# d = datetime.strptime(fecha_1,"%d/%m/%Y")
d = datetime.strptime(fecha_hora,"%d/%m/%Y %I:%M:%S %p")

print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())