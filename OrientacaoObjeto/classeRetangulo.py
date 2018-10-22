class Retangulo:
    def __init__(self, x, y):
        """construtor da classe"""
        self.x = x
        self.y = y

    def mudarValorDosLados(self, newx, newy):
        self.x = newx
        self.y = newy

    def __str__(self):
        return "Ponto x: ({}) Ponto y: ({})".format(self.x, self.y)

    def calculaArea(self):
        return self.x * self.y

    def calculaPerimetro(self):
        return 2 * (self.x + self.y)


novoRetangulo = Retangulo(100, 70)
print(novoRetangulo)
print(novoRetangulo.calculaArea())
print(novoRetangulo.calculaPerimetro())

