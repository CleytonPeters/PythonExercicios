class Cubo:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def mostraValorDosLados(self):
        return "comprimento" + self.x + "altura" + self.y + "volume" + self.z
    def mudaValorDosLados(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def calculaVolume(self):
        return self.x * self.y * self.z
    def __str__(self):
        return "É um cubo"