def parimpar(x):
    if x % 2 == 0:
        return "Par"
    elif x % 2 != 0:
        return "Impar"

x = int(input("Par ou Impar? "))
print (parimpar(x))