class No:
    def __init__(self, dado=None, proximo=None):
        self.dado = dado
        self.proximo = proximo

    def __str__(self):
        return str(self.dado)


class Fila(object):
    def __init__(self):
        self.dados = []

    def insere(self, elemento):
        self.dados.append(elemento)

    def retira(self):
        return self.dados.pop(0)

    def vazia(self):
        return len(self.dados) == 0


class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

class Arvore :
  def __init__(self, cargo, left=None, right=None) :
    self.cargo = cargo
    self.left  = left
    self.right = right

  def __str__(self) :
    return str(self.cargo)




