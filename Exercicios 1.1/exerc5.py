#5) Toda vez que um homem traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# Escreva uma função que recebe como parâmetro o peso (peso de peixes) e calcule o excesso.
# Retorne a quantidade de quilos além do limite e o valor da multa que ele deverá pagar.


def calculaExcesso(peso):
    excesso = peso - 50

    return excesso


pesoPeixe = input ("digite o valor de kgs: ")
peso = int(pesoPeixe)

print (calculaExcesso(peso))

print (calculaExcesso(peso * 4))