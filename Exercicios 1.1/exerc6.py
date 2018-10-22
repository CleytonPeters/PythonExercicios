#6) Implemente uma função que recebe quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre (com print) o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

x = input("Digite quantos você ganha por hora:")
y = input("Digite quantas horas você trabalha no mês:")
salarioHora = float(x)
horasTrabalhadas = float(y)
salario = salarioHora * horasTrabalhadas
bruto = salario
descontos = salario * 0.24
ir = bruto * 0.08
inss = bruto * 0.11
sindicato = bruto * 0.05


liquido = bruto - descontos
print("Seu salário bruto é de: ", bruto)
print("Seu salário liquido é de: ", liquido)
print("Sindicato: ", sindicato)
print("INSS: ", inss)
s = "Imposto de Renda %.2f" % (ir)
print(s)

