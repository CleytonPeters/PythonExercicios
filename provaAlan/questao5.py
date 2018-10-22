def torre(n):
    for i in range(n+1):
        print(str(i) * i)
        i = i + 1
e = int(input("Digite um numero "))
torre(e)