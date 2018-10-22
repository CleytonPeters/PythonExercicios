def corrigirFone(n):
    if len(n) == 8:
        num = '9' + n[:4] + '-' + n[4]
        print(num)
    elif len(n) == 9 and n [5:6] != '-':
        num = n[:5] + '-' + n[5:]
        print(num)
    elif len(n) == 9 and n[5:6] == '-':
        num = '9' + n[0]
        print(num)
    else:
        print(n)

n = int(input("telefone: "))
print(corrigirFone(n))