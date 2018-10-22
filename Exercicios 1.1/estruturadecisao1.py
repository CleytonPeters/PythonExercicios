#1) Faça uma função que verifique se uma letra passada como parâmetro é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido


def gender(sexo):
    if sexo.upper() == 'M':
        return print("Sexo Masculino")
    elif sexo.upper() == 'F':
        return print("Sexo Feminino")
    else:
        return print("Sexo Inválido")


s = input("Type F for female or M for Male: ")

gender(s)


