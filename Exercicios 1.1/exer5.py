#5) Implemente uma função para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#  que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#  mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#  A função deverá receber o valor da sua hora e a quantidade de horas trabalhadas no mês.



qtdHora = float(input("Valor Hora: "))
salHora = float(input("Horas Mês: "))
calculaFolha(qtdHora, salHora)
print("Bruto", bruto)
print("(-) INSS (10%)     : R$", vlr_inss)
print("IR", vlr_ir)
print("FGTS (11%)         : R$", vlr_fgts)
print("Total de Descontos : R$", vlr_desconto)
print("Salário Liquido    : R$", vlr_liquido)

def calculaFolha(qtdHora, salHora):
    bruto = qtdHora * salHora
    vlr_inss =  bruto *  10 / 100
    vlr_ir =  impostoRenda(bruto)
    vlr_fgts = bruto *  11 / 100
    vlr_sind = bruto *  3 / 100
    vlr_desconto = vlr_inss + vlr_ir + vlr_sind
    vlr_liquido = bruto -  vlr_desconto
    return bruto,  vlr_inss, vlr_ir, vlr_fgts, vlr_sind,  vlr_liquido, vlr_desconto

def impostoRenda(bruto):
    if bruto <= 900:
        ir = bruto*0
        return ir
    elif bruto <= 1500:
        ir = bruto*0.05
        return ir
    elif bruto <= 2500:
        ir = bruto*0.10
        return ir
    elif bruto > 2500:
        ir = bruto*0.20
        return ir







