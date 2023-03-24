from TipoCarro import TipoCarro
from Carro import carro

tipo_carro=TipoCarro("Camiontea","carga","vehiculo de doble traccion") 
print("-----------------------------")
tipo_carro.setTipo("camion")
tipo_carro.setUso("transporte de carga")
tipo_carro.setDescripcion("Volo")
print("-----------------------------")
print(tipo_carro.getTipo())
print(tipo_carro.getUso())
print(tipo_carro.getDescripcion())
print("-----------------------------")
print("***Carros***")
carro=carro("camioneta","Transporte","familiar","2023","negro","NHTP2","Chevoret","10","Principal")
print(carro.getColor())
print(carro.getMarca())
print(carro.getModelo())
print(carro.getPlaca())
print(carro.getUnidades())
print(carro.getSucursal())
print(carro.contador)



