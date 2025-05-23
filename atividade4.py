lista = []

def menu():
    
    print("Bem Vindo Ao Menu".center(30, '-'))
    print("1 - Cadastrar Usuarios")
    print("2 - Historico de pessoas cadastradas")
    print("3 - Sair")
    print("-----------------------------------")
    c = 0    
        
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            print("--------------------------------")
            return opcao
        except ValueError:
            print("Opção invalida. Tente novamente.")
            
def cadastro():
     
    print("CADASTRO".center(30, '-'))
    print("Digite o nome que deseja cadastrar: ")
    print("Digite a idade que deseja cadastrar: ")
            