valor = float(input("Digite o valor da compra: "))
cupom = input("Possui cupom de desconto?: ")

if(cupom == "sim" or valor >= 200 ):
    print("Você ganhou um desconto de 15%! ")
else:
    print("Você não tem direito a descontos no momento! ")