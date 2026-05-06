vetor = []
num_digitado = 0

for i in range(8):
    num = int(input("Digite um número: "))
    vetor.append(num)

num_digitado = int(input("Digite um novo número: "))

for i in range(8):
    if(vetor[i] == num_digitado):
        print("Encontrou")
else:
    print("Não encontrado")