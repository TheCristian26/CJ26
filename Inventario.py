class Inventario():
    def __init__(self, unidades , sucursal) :
        self.__unidades=unidades
        self.__sucural=sucursal
    
    def getUnidades(self):
        return self.__unidades
    
    def getSucursal(self):
        return self.__sucural
    
    def setUnidades(self,unidades):
        self.__unidades=unidades

    def setsucursal(self,sucursal):
         self.__sucural=sucursal