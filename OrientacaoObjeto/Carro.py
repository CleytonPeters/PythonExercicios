class Carro:
    def __init__(self):
        self.combustivel = 0

     def consumo(self, distancia, consumo):
         self.litros = distancia / consumo
     def andar(self, anda):
         self.litros = anda


     def obterGasolina(self):
         return ("Nivel de combustivel: { } ", format(combustivel))
     def adicionarGasolina(self, litros):
         self.litros = litros
