#3) Implemente uma função que peça a temperatura em graus Farenheit, transforme e retorne a temperatura em graus Celsius.
#   $C = (5 * (F-32) / 9)$

def conversor(x):
    celsius = (x - 32) / 1.8
    return celsius

x = int(input("Digite o valor em Farenheit: "))

print ("O valor em graus celsius é de : ", conversor(x))