programa {
  funcao inicio() {
    real baseMaior, baseMenor, altura, area

    escreva("BaseMaior: ")
    leia(baseMaior)

    escreva("BaseMenor: ")
    leia(baseMenor)
    
    escreva("altura: ")
    leia(altura)
    
    area = ((baseMaior+baseMenor)*altura)/2
    escreva("Área do trapésio: ", area)

  }
}
