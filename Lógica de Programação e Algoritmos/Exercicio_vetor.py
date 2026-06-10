vetor = []
qtd_pares = 0
qtd_impares = 0

for i in range(10):
    vetor.append(int(input("Digite um número: ")))

for num in vetor:
    if(num % 2 == 0):
        qtd_pares+=1
    else:
        qtd_impares+=1
        print("A Qtd de pares é: ", qtd_pares, "\n Qtd ímpares ", qtd_pares)