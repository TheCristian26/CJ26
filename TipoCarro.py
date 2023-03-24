class TipoCarro:
    def __init__(self , tipo , uso , descripcion,detalles):
         self.__tipo= tipo
         self.__uso= uso
         self.__descripcion= descripcion
         

    #GETTERS SOLO FUNCIONES

    def getTipo(self) :
         return self.__tipo
    
    def getUso(self) :
         return self.__uso
    
    def getDescripcion(self) :
         return self.__descripcion
    
    #Setter Asigna 
    def setTipo(self,tipo) :
         self.__tipo = tipo
    
    def setUso(self,uso) :
         self.__uso = uso

    def setDescripcion(self,descripcion) : 
         self.__descripcion = descripcion
         
     #def getDetalles(self):
         #detalles = {
          #    "Tipo" self.__tipo,
           #   " Uso " self.__uso,
            #  " Descripcion"self.__descripcion
         #}
         #return detalles
         
         
         

