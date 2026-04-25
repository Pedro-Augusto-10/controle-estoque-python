estoque = {}

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    estoque[nome] = quantidade
    print("Produto adicionado com sucesso!\n")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.\n")
    else:
        for produto, qtd in estoque.items():
            print(f"{produto}: {qtd}")
    print()

def atualizar_produto():
    nome = input("Nome do produto: ")
    if nome in estoque:
        quantidade = int(input("Nova quantidade: "))
        estoque[nome] = quantidade
        print("Produto atualizado!\n")
    else:
        print("Produto não encontrado.\n")

def remover_produto():
    nome = input("Nome do produto: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto removido!\n")
    else:
        print("Produto não encontrado.\n")

while True:
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")