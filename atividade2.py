lista = []

itens = int(input("Quantos itens deseja adicionar a lista? "))
c = 0

while True:
    
    if c < itens:
        try:
            nome = input("Digite o nome do produto: ")
            
                
            produto = {"nome": nome}
            lista.append(produto)
            
            c = c + 1 
        except ValueError:
            print("Valores invalidos. Digite novamente.")
            
    else:
        print("---------------------------------")
        break
    
if not lista:
    print("Nenhum item registrado")
else:
    print(f"Quantidade de itens registrados: {len(lista)}")
    for produto in lista:
        print(f"Nome: {produto['nome']}")
print('-'*40)
