programa {
  funcao inicio() {
    inteiro idade

    escreva("Digite sua idade: ")
    leia(idade)

    se(idade >= 0 e idade <= 12){
    escreva("Criança")
    }
    senao se(idade >= 13 e idade <= 17){
      escreva("Adolecente")
    }
    senao se(idade >= 18 e idade <= 59){
      escreva("Adulto")
    }
    senao se(idade >= 60){
      escreva("Idoso")
    }
  }
}
