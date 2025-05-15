from avl import AVLUsuarios

def menu():
    print("\nMENU DO SISTEMA AVL ")
    print("1. Cadastrar usuário")
    print("2. Remover usuário")
    print("3. Buscar usuário")
    print("4. Listar usuários em ordem alfabética")
    print("5. Sair")
    print("=================================")

if __name__ == "__main__":
    sistema = AVLUsuarios()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            id = int(input("ID: "))
            email = input("E-mail: ")
            sistema.raiz = sistema.inserir(sistema.raiz, nome, id, email)
            print(f"Usuário '{nome}' cadastrado com sucesso.")

        elif opcao == "2":
            nome = input("Nome do usuário a ser removido: ")
            sistema.raiz = sistema.remover(sistema.raiz, nome)
            print(f"Usuário '{nome}' removido (se existia).")

        elif opcao == "3":
            nome = input("Nome do usuário a buscar: ")
            usuario = sistema.buscar(sistema.raiz, nome)
            if usuario:
                print(f"Usuário encontrado:\nNome: {usuario.nome}, ID: {usuario.id}, Email: {usuario.email}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            print("\nUsuários cadastrados (ordem alfabética):")
            sistema.listar_em_ordem(sistema.raiz)

        elif opcao == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")
