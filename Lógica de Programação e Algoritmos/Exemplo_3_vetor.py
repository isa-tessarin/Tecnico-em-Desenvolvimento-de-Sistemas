#Alternativa de forma 1
print("----------------------------------")
numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

maior = -9999999999999999999999999999999999
for numero in numeros:
    if(numero > maior):
        maior = numero
print("O maior número é: ", maior)
#Alternativa de forma 2
print("----------------------------------")
maior = numeros[0]

for numero in numeros:
    if(numero > maior):
        maior = numero
print("O maior número é: ", maior)