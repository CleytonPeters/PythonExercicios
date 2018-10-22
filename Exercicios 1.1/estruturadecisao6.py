#6) Implemente uma função que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem formar um triângulo ou não.
#  Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

def triangulo():
    valor1 = float(input("Digite um numero: "))

    valor2 = float(input("Digite um numero: "))

    valor3 = float(input("Digite um numero: "))

    if valor1 == valor2 and valor2 == valor3:
        print("Equilátero")
    elif valor1 == valor2 and valor1 != valor3 or valor1 != valor2 and valor2 == valor3:
        print("Isósceles")
    else:
        print("Escaleno")

triangulo()


