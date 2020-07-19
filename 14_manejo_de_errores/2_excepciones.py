#Tratando más de un tipo de excepción

#Ejemplo: Abrir un archivo de texto plano,
#leer la primera línea y ubicarla en un diccionario
while True:
    try:
        break
        f = open("registro1.txt","r")
        d = {"nombre":"Daniel","curso":"Python","secciones":3}
        for l in f:
            print(l,d[l])
    except FileNotFoundError as e:
        print("El archivo no existe")
    except KeyError as e:
        print("No se encuentra la clave",e)
    except Exception as e:
        print(e)
    else:
        print("Todo ok!")
        f.close()
    finally:
        print("Fin de un conjunto instrucciones")

    


