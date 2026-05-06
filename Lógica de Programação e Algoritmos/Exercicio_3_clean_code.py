numeros = []

for i in range(4):
    numeros.append(float(input(f"Digite o {i+1}º número:")))
    
Media = sum(numeros)/len(numeros)

print("Sua Média é: ", Media)