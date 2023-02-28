
class TV:
    numTV = 0
    def __init__(self, marca,  estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._estado = estado
        self._control = None #para tomar en cuenta/ cuando no se le quiere asignar valor con el constructor se una None (o eso parece)
        TV.numTV += 1
    
    def getMarca(self):
        return self._marca
    def getCanal(self):
        return self._canal
    def getPrecio(self):
        return self._precio
    def getVolumen(self):
        return self._volumen
    def getNumTV(self):
        return TV.numTV
    def getEstado(self):
        return self._estado
    def getControl(self):
        return self._control
  
    def setMarca(self, marca):   
        self._marca = marca
    def setControl(self, control):
        self._control = control
    def setPrecio(self, precio):
        self._precio = precio
    def setNumTV(self, numTV):
        TV.numTV = numTV
    

    def setCanal(self, canal):
        if (self._estado == True and canal >= 1 and canal <= 120):
            self._canal = canal
    def setVolumen(self, volumen):
        if (self._estado == True and volumen >= 1 and volumen <= 7):
            self._volumen = volumen
    
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if (self._estado == True and self._canal >= 1 and self._canal < 120):
            self._canal += 1
    def canalDown(self):
        if (self._estado == True and self._canal > 1 and self._canal <= 120):
            self._canal -= 1
    def volumenUp(self):
        if (self._estado == True and self._volumen >= 1 and self._volumen < 7):
            self._volumen += 1
    def volumenDown(self):
        if (self._estado == True and self._volumen > 1 and self._volumen <= 7):
            self._volumen -= 1

        