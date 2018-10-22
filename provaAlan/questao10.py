class Fila:
    def __init__(self):
        self.cabeca = None
        self.calda = None
        self.size = 0
    def tamanho(self):
        return self.size
    def insere(self, elemento):
        if self.size == 0:
            self.cabeca = elemento
            self.calda = elemento
        else:
            self.calda.proximo = elemento
            self.calda = elemento
        self.size++
    def remove(self):
        if self.size == 0:
            print("Evvo..")
        elif.self.size == 1:
            primeiro = self.cabeca
            self.cabeca = None
            self.calda = None
            self.size = 0
            return primeiro
        else:
            primeiro = self.cabeca
            self.cabeca = primeiro.prox
            self.size --
            return primeiro