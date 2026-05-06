#Criando uma variavel número
numero = 10

# Criando uma variavel textual
nome = "Isadora"

#Usuario inserir um texto
nome_completo = input("Digite seu nome:")

#Usuario inserir um número inteiro
idade = int(input("Digite um número: "))

#Usuario inserir um número decimal
Salario = float(input("Digite o salario"))

#Estruturas condicionais
if(Salario > 1500 and idade >= 18):
    print("Você pode tirar CNH: ")
elif(Salario < 1500 or idade < 18):
    print("Você não pode tirar CNH")
else:
    print("Invalido")

#Estruturas condicionais exemplo 2

turno = input("Digite seu turno (M/N/V)")

if(turno == "M"):
    print("Bom dia")
elif(turno == "V"):
    print("Boa tarde!")
elif(turno == "N"):
    print("Boa noite!")
else:
    print("Invalido")

#Estrutura de repetição
#0 -> 10
for i in range(11):
    print(i)

# 1 - 15
for i in range(1,16):
    print(i)

# 5 -> 65(aumentando de 5 em 5)
for i in range(5,66,+5):
    print(i)

#122 -> 0 (tirando de 2 em 2)
for i in range(122,-1,-2):
    print(i)

#Usuario escolhe o inicio e fim
# inicio e fim

inicio = int(input("inicio: "))
fim = int(input("fim"))

for i in range(inicio,fim+1):
    print(i)

#Vetores

nomes = []

#sempre utilizar para preencher o vetor
for i in range(5):
    nomes.append(int(input("Digite um nome: ")))

#sempre utilizar para exibir o vetor
for nome in nomes:
    print(nome)