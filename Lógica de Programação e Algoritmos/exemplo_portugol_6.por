programa {
  funcao inicio() {
    real raio, area, altura, volume, pi = 3.14

    escreva("Digite o raio:")
    leia(raio)

    escreva("Digite a altura: ")
    leia(altura)

    area = 2*pi*raio*(raio+altura)
    escreva("\n Área = ", area)

    volume = pi*raio*raio*altura
    escreva("\n Volume = ", volume)

  }
}
