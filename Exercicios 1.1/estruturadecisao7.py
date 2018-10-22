#7) Implemente uma função que recebe uma data no formato dd/mm/aaaa e retorna True/False
#  se a mesma é uma data válida/inválida.

def data()
    dia = int(input("Digite o Dia: "))

    mes = int(input("Digite o Mês: "))

    ano = int(input("Digite o Ano: "))

    if dia > 31:
        print("Inválido")
    elif mes > 12:
        print("Inválido")

data()