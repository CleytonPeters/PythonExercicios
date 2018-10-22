#3) Faça uma função para ajudar o professor Fachini a calcular as notas dos seus queridos alunos.
#  A função deve receber como parâmetro as 3 notas de um estudante.
#  A função deve calcular a média alcançada pelo aluno e apresentar:

nota1 = float(input("Nota 1 é: "))
nota2 = float(input("Nota 2 é: "))
nota3 = float(input("Nota 3 é: "))
soma = (nota1 + nota2 + nota3) / 3

if (soma == 10):
    print("Aprovado com Distinção")
elif (soma >= 6):
    print("Aprovado")
elif (soma <= 5.9999999):
    print("Reprovado")