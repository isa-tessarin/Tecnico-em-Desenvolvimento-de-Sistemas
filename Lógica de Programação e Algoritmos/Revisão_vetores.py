# Revisão vetores
# Solicitar ao usuario a quantidade de números
# preencher vetor e calcular a soma dos números
# exibir soma
# -------------------------------------

qtd= int(input("Digite a quantidade: "))
soma = 0
vetor = []

for i in range(qtd):
    vetor.append(int(input("Digite vetor: ")))

for num in vetor:
    soma = soma + num

print(soma)