num1 = float(input("digite um número: "))
num2 = float(input("digite um número: "))
num3 = float(input("digite um número: "))

if((num1+num2)>num3 and (num1+num3)>num2 and (num2+num3)>num1):
    if(num1 == num2 and num2 == num3 and num3 == num1):
        print("Equilátero")
    elif(num1 != num2 and num2 != num3 and num3 != num1):
        print("Escaleno")
    else:
        print("isósceles")
else:
    print("O triangulo não existe")

