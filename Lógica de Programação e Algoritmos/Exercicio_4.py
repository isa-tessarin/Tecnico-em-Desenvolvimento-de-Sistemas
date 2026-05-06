tempo_inicial = float(input("digite o tempo inicial: "))
tempo_final = float(input("Digite o tempo final: "))
posicao_inicial = float(input("Digite a posição inicial: "))
posicao_final = float(input("Digite a posição final:"))

Vm = (posicao_final - posicao_inicial)/(tempo_final - tempo_inicial)

print("a velocidade média é:", Vm)