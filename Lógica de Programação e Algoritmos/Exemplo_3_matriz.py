linhas = int(input("Quantidade de linhas: "))
colunas = int(input("Quantidade de colunas: "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"M[{i}][{j}] = ")))
    matriz.append(linha)

print("Matriz soma: ")
for linha in matriz:
    print(linha)