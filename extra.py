lista = []

def cadastro():
    c = 0
    idade = 0

    while c < 2:
        c = c + 1

        nome = input("Digite seu nome completo: ")
        while not nome:
            print("Erro: O nome completo nao pode esta vazio.")
            nome = input("Digite seu nome completo: ").strip()

        palestra = input("Digite o nome da palestra: ")
        while not palestra:
            print("Erro: O compo nao pode esta vazio.")
            palestra = input("Digite o nome da palestra: ").strip()

        while True:
            try:
                ano = int(input("Digite o ano de nascimento: "))
                if ano < 1900 or ano > 2025:
                    print("Digite um ano valido entre 1900 e 2025.")
                else:
                    break
            except ValueError:
                print("Digite um valor valido.")

            idade = 2025 - ano
        

        usuario = {"nome": nome, "palestra": palestra, "idade": idade}
        lista.append(usuario)
        print("Usuário cadastrado com sucesso!")

    if not lista:
        print("Nenhum usuario cadastrado.")

    else: 
        for usuario in lista:
            print(f"Nome: {usuario['nome']} | Palestra: {usuario['palestra']} | Idade: {usuario['idade']} ")
            

cadastro()