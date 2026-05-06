inicio = int(input("digite um número inicial: "))
fim = int(input("digite um número final: "))
soma = 0
for i in range(inicio,fim+1):
    if(i%2 == 0):
        soma = soma + i

print("A soma é: ", soma)