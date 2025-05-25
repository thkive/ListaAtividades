#primeiro foi criado uma lista vazia para ser armazenada todas as informaçoes
lista = []
# uma funçao menu para que o usuario escolha uma opcao
def menu():
    
    print("Bem Vindo Ao Menu".center(30, '-'))
    print("1 - Cadastrar Usuarios")
    print("2 - Historico de pessoas cadastradas")
    print("3 - Sair")
    print("-----------------------------------")
    c = 0    
# o try e o except sao usados para caso o usuario digite um 
# valor errado ele dar erro e pede para tentar novamemte
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            print("--------------------------------")
            return opcao
        except ValueError:
            print("Opção invalida. Tente novamente.")
# aqui foi criada um funçao para pedir ao usuario as informaçoes necessarias
# e guardar elas
def cadastro():
    print("CADASTRO".center(30, '-'))
     
    while True:
         
        nome = input("Digite o nome que deseja cadastrar: ")
        try:
            idade = int(input("Digite a idade que deseja cadastrar: "))
        except ValueError:
            print("Idade invalida. Tente novamente.")
# lista.append serve para tudo que for digitado em usuario 
# seja salvo dentro da lisa criada no inicio
        usuario = {"nome": nome, "idade": idade}
        lista.append(usuario)
        print("Usuário cadastrado com sucesso!")

# strip remove espaços em branco no começo e no final da string
# lower serve para se uma pessoa digitar a resposta em letra maiuslo ele deixa ela em minuscula,
# sem dar erro no programa
        continuar = input("Deseja cadastrar outro usuário? (s/n): ").strip().lower()
        if continuar != 's':
            print("Cadastro encerrado")
            break
            
# essa fuçao foi criada para mostrar tudo que foi guardado na lista
def historico():
    soma = 0
    print("HISTORICO".center(30, '-'))
# if not lista ele vai analisar a lista para ver se tem algum valor 
# dentro dela, se nao tiver ele roda essa linha 
    if not lista:
        print("Nenhum usuario cadastrado")
    else:
# o len vai contar quantos valores tem armazenados na lista
        print(f"Quantas pessoas cadastradas: {len(lista)}")
        for usuario in lista:
            print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")
# essa linha vai calcular a media de idade armazenadas na lista 
    for usuario in lista:
        soma = soma + usuario["idade"]
    media = soma / len(lista)
    print(f"A media de idades é: {media:.2f}")
# essa linha vai calcular a maior idade armazenada dentro da lista
    mais_velho = lista[0]
    for usuario in lista:
        if usuario["idade"]> mais_velho["idade"]:
            mais_velho = usuario
    print(f"Pessoa mais velha: {mais_velho['nome']} com {mais_velho['idade']} anos")
# essa funçao vai ser usada para jumtar todas as outas em um lugar só
def sistema():

    while True:

        opcao = menu()

        if opcao == 1:
            cadastro()
        elif opcao == 2:
            historico()
        elif opcao == 3:
            print("Saindo do sistema. Volte sempre.")
            break
        else:
            print("Opção Invalida. Tente Novamente.")
# final chamamos a funçao sistema para ela rodar todos juntos
sistema()
