#2) Faça uma função que verifique se uma letra passada como parâmetro é vogal ou consoante.


def vogal(letra):
    if letra.upper() == 'A':
        return print("Vogal")
    elif letra.upper() == 'E':
        return print("Vogal")
    elif letra.upper() == 'I':
        return print("Vogal")
    elif letra.upper() == 'O':
        return print("Vogal")
    elif letra.upper() == 'U':
        return print("Vogal")
    else:
        return print("Consoante")

valor = input("Digite uma letra para saber se é vogal ou consoante: ")
vogal(valor)