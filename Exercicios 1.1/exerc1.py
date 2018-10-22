##1) Implemente um método que converta metros para centímetros.

def converte (x):
    metros = x*100
    return metros

x = int(input("Digite metros: "))

print("Em CM: ", converte(x))
