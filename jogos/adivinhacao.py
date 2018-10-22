print ("*************************************")
print ("Olá, bem vindo ao jogo de adivinhação")
print ("*************************************")
correto = 44

chute = input ("Chute um número: ")
numero = int(chute)

errou = numero != correto


while (errou):
    i = 10
    while(i > 0):
        print ("Sua tentativa número: ", i)

        maior = numero > correto
        menor = numero < correto
        acertou = numero == correto

        if(maior):
            print ("Você errou, seu chute foi maior que o numero secreto!")

        elif(menor):
            print ("Você errou, seu numero foi menor que o numero secreto!")

        chute = input("Tente Novamente: ")
        numero = int(chute)

        if(acertou):
            print("Você acertou miseravel!")
            exit()

        i = i - 1

    print ("Fim de jogo(GameOver)")
    exit()

