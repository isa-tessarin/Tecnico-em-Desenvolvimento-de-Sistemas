programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3

    escreva("Escreva lado 1: ")
    leia(lado1)

    escreva("Escreva lado 2: ")
    leia(lado2)

    escreva(" Escreva lado 3: ")
    leia(lado3)

    se(lado1 == lado2 ou lado2 == lado3 e lado3 == lado1 ){
    escreva("Equilátero")
    }

    senao se(lado1 == lado2 ou lado2 == lado3 ou lado3 == lado1){
      escreva("isósceles")
    }
    senao se(lado1 != lado2  e lado2 != lado3 e lado3 != lado1){
      escreva("Escaleno")
    }
  }
}
