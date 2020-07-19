class auto:
    """Esta clase define las propiedades de un auto"""
    def __init__(self,cnt_neumaticos,cnt_asientos,num_placa,marca,color,cnt_combustible):
        self.cantidad_neumaticos= cnt_neumaticos
        self.cantidad_asientos = cnt_asientos
        self.numero_placa = num_placa
        self.marca = marca
        self.color = color
        self.cantidad_combustible = cnt_combustible



chevrolet_abc_123 = auto(4,4,"ABC-123","Chevrolet","gris",1.5)
print(chevrolet_abc_123)
print(chevrolet_abc_123.marca)
print(chevrolet_abc_123.color)


auto_2 = auto(4,4,"ABD-123","Chevrolet","rojo",2.5)
auto_3 = auto(8,4,"ABM-123","Chevrolet","verde",1)