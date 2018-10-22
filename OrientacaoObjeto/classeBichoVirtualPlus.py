class BichoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = True
        self.saude = 100
        self.idade = 25

    def com_fome(self):
        if self.fome:
            return "Com fome"
        else:
            return "Sem fome"

novoBicho = BichoVirtual("Tamaguchi")
print(novoBicho.nome)
novoBicho.fome = False
print(novoBicho.com_fome())
print(novoBicho.idade)
print(novoBicho.saude)
