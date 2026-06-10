matriz = []
maiores_que_5 = 0
for i in range(2):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)
for linha in matriz:
    print(matriz)
for i in range(2):
    for j in range(3):
        if(matriz[i][j] > 5):
            maiores_que_5 = maiores_que_5 + 1
print("Maiores que 5: ", maiores_que_5)