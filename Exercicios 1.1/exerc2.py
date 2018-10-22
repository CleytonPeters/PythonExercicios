#2) Implemente uma função que recebe o raio de um círculo, calcule e retorna sua área.
from math import pi


def areaCirculo(x):
    raio = x**2 * pi
    return raio

x = float(input("Digite o tamanho do raio: "))

print ("o valor da area é de : ", areaCirculo(x))