p_normal = 55
descuento = 0.1534
p_ahora = 49.5
plantilla = """El precio normal del producto ABC es de S/ {:8.3f} y con el descuento del {:.2%} el precio ahora es de S/ {:8.3f}"""

mensaje = plantilla.format(p_normal,descuento,p_ahora)

print(mensaje)

#Otras formas de insertar datos
#Si se define de forma explicita el nombre de la variable dentro de la plantilla, no importa el orden en que se pasan los parámetros en el método format.
plantilla = """El precio normal del producto ABC es de S/ {p_normal:8.3f} y con el descuento del {descuento:.2%} el precio ahora es de S/ {p_ahora:8.3f}"""
mensaje = plantilla.format(p_normal=p_normal,descuento=descuento,p_ahora=p_ahora)
mensaje = plantilla.format(p_normal=p_normal,p_ahora=p_ahora,descuento=descuento)
mensaje = plantilla.format(descuento=descuento,p_normal=p_normal,p_ahora=p_ahora)

#Llamada através del indice de ubicación de los parámetros en el método format
plantilla = """El precio normal del producto ABC es de S/ {0:8.3f} y con el descuento del {1:.2%} el precio ahora es de S/ {2:8.3f}"""
mensaje = plantilla.format(p_normal,descuento,p_ahora)
print(mensaje)

