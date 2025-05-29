def doacao():

    print("------CAIXA DE DOAÇÃO DE ALIMENTOS------")

    while True:

        try:
            valor_str = input("Digite quantos quilos(kg) deseja doar: ")
            print("---------------------------------")
        except ValueError:
            print("Digite um valor valido.")

        if valor_str.isdigit():
            valor = int(valor_str)
        
        else:
            print("Entrada invalida. Digite apenas numeros inteiros.")
            continue

        if valor < 1:
            print("Valor invalido. Só aceitamos doação acima de 1kg.")
        else: 
            break

    quilos = [5, 2, 1]

    print(f"Embalando doação de {valor}kg")

    for quilo in quilos:
        quantidade = valor // quilo
        valor = valor % quilo
        if quantidade > 0:
            print(f"Sera usado para embalar {quantidade} pacote de {quilo}kg")

    print(f"Obrigada pela doação. Tenha uma otimo dia.")
    print("---------------------------------------")

doacao()