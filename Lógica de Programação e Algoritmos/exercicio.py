nomes = []
for i in range(6):
    nomes.append(input("Digite um nome: "))
nome_buscar = input("Digite o nome que gostaria de buscar: ")
for nome in nomes:
    if(nome == nome_buscar):
        print("Encontrou!")
    elif(nome != nome_buscar):
        print("Não existe!")