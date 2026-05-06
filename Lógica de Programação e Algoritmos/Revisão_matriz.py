# Revisão Matriz 1
# Solicitar a quantidade de linhas
# Solicitar a quantidade de colunas
# Preencher a Matriz
# Calcular a soma de todos os números
# ----------------------------------------

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas"))
matriz = []
soma = 0

# Sempre Preencher matriz
for i in range(linhas):
    linha=[]
    for j in range(colunas):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)

for i in range(linhas):
    for j in range(colunas):
        soma = soma + matriz[i][j]
print("A soma é ", soma)