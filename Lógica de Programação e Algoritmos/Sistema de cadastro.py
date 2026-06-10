# Sistema de cadastro de usuários e produtos
# O sistema deverá permitir:
# - Cadastrar
# - Listar
# - deletar

# Criação das listas
usuarios = []
produtos =[]

# ------------------------------------------------
# ------------ Função Menu Usuarios --------------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("-------- Menu Usuarios --------")
        print("1 - Cadastrar Usuários")
        print("2 - Listar Usuários")
        print("3 - Deletar Usuários")
        print("4 - voltar")

        opcao_menu_usuario = int(input("Escolha uma opção: "))
        match opcao_menu_usuario:
            # Cadastrar Usuario
            case 1:
                nome = input("Digite o nome: ")
                telefone = (input("Digite o telefone: "))
                email = input("Digite o email: ")
                # Criação do json de usuarios (chave: valor)
                usuario = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                }

                # Adicionar o json no array
                usuarios.append(usuario)
                print(f"Usuario {usuario['nome']} cadastro com sucesso")
            # Listar Usuários
            case 2:
                print("\n Lista de Usuários: ")

                if(len(usuarios) == 0):
                    print("Nenhum Usuário cadastrado! ")
                else:
                    for usu in usuarios:
                        print("--------")
                        print("nome ", usu["nome"])
                        print("telefone ", usu["telefone"])
                        print("Email ", usu["email"])
            # Deletar usuario
            case 3:
                nome_deletar = input("Digite o nome do usuario que deseja deletar: ")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("Usuario removido com sucesso! ")
                if(encontrado == False):
                    print("usuario não encontrado")

            # voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break
# ------------------------------------------------
# ------------ Função Menu Usuarios --------------
def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_produto != 5):
        print()
        print("-------- Menu produtos --------")
        print("1 - Cadastrar produtos")
        print("2 - Listar produtos")
        print("3 - Deletar produtos")
        print("4 - calcular")
        print("5 - voltar")

        opcao_menu_produto = int(input("Escolha uma opção: "))
        match opcao_menu_produto:
            # Cadastrar produto
            case 1:
                nome = input("Digite o nome: ")
                descricao = (input("Digite a descrição: "))
                quantidade = input("Digite a quantidade: ")
                valor = input("Digite o valor: ")
                # Criação do json de produto (chave: valor)
                produto = {
                    "nome": nome,
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "valor": valor
                }

                # Adicionar o json no array
                produtos.append()
                print(f"produto {produto['nome']} cadastro com sucesso")
            # Listar Usuários
            case 2:
                print("\n Lista de produtos: ")

                if(len(produtos) == 0):
                    print("Nenhum produto cadastrado! ")
                else:
                    for pro in produtos:
                        print("--------")
                        print("nome ", pro["nome"])
                        print("descrição ", pro["descricao"])
                        print("quantidade ", pro["quantidade"])
                        print("valor ", pro["valor"])
            # Deletar usuario
            case 3:
                nome_deletar = input("Digite o nome do produto que deseja deletar: ")
                encontrado = False

                for pro in produtos:
                    if(pro["nome"] == nome_deletar):
                        produtos.remove(pro)
                        encontrado = True
                        print("produto removido com sucesso! ")
                if(encontrado == False):
                    print("produto não encontrado")
                    
            # voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break
                
# ------------------------------------------------
# ---------------- Menu Principal ----------------
opcao_menu = 0
while(opcao_menu != 3):
    print("------ Menu - Sistemas de Cadastro ------")
    print("Opções")
    print("1 - Usuários")
    print("2 - Produtos")
    print("3 - Sair")
    opcao_menu = int(input("Digite uma opção: "))

    match opcao_menu:
        # Menu usuarios
        case 1:
            menu_usuarios()
        # Menu produtos
        case 2:
            menu_produtos()
        case 3:
            print("Até logo")
        case _:
            print("Opção invalida")
        