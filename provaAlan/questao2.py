def idade(x):
    if x < 15:
        return "criança"
    elif x < 18:
        return "adolescente"
    elif x < 30:
        return "jovem"
    elif x < 50:
        return "adulto"
    return x

x = int(input("Sua Idade: "))
print(idade(x))