from TipoCarro import(TipoCarro)
from Inventario import Inventario
class carro(TipoCarro,Inventario):
    contador=0;
    def __init__(self, modelo , color , placa , marca , tipo , uso , descripcion,unidades,sucursal) :
        TipoCarro.__init__(self,tipo,uso,descripcion)
        Inventario.__init__(self,unidades,sucursal)
        self.__modelo=modelo
        self.__marca=marca
        self.__color=color
        self.__placa=placa
        carro.contador +=1

    def getModelo(self):
        return self.__modelo
    
    def getMarca(self):
        return self.__marca
    
    def getPlaca(self):
        return self.__placa
    
    def getColor(self):
        return self.__color
    
    def setModelo(self,modelo):
        self.__modelo=modelo
    
    def setModelo(self,marca):
         self.__modelo=marca
    
    def setPlaca(self,placa):
         self.__placa=placa
    
    def setColor(self,color):
         self.__color=color
        