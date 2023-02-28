
class Control:
    def __init__(self):
        self._tv = None
    
    def getTv(self):
        return self._tv
    def setTV(self, tv):
        self._tv = tv

    def enlazar(self, tv):
        self._tv = tv
        tv._control = self
    
    def turnOn(self):
        self._tv._estado = True
    def turnOff(self):
        self._tv._estado = False

    def canalUp(self):
        if (self._tv._estado == True and self._tv._canal >= 1 and self._tv._canal < 120):
            self._tv._canal += 1
    def canalDown(self):
        if (self._tv._estado == True and self._tv._canal > 1 and self._tv._canal <= 120):
            self._tv._canal -= 1
    def volumenUp(self):
        if (self._tv._estado == True and self._tv._volumen >= 1 and self._tv._volumen < 7):
            self._tv._volumen += 1
    def volumenDown(self):
        if (self._tv._estado == True and self._tv._volumen > 1 and self._tv._volumen <= 7):
            self._tv._volumen -= 1
    
    def getCanal(self):
        return self._tv._canal
    def setCanal(self, canal):
        if (self._tv._estado == True and canal >= 1 and canal <= 120):
            self._tv._canal = canal