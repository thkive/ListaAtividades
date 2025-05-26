saldo = 500
valor = int(input("Digite o valor que deseja sacar: "))

while valor > saldo:
    print("Saldo insuficiente, tente novamente.")
    valor = int(input("Digite o valor que deseja sacar: "))

notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

notas_10 = valor // 10
valor = valor % 10

notas_5 = valor // 5
valor = valor % 5

notas_2 = valor // 2
valor = valor % 2

if notas_100 > 0:
    print(f"{notas_100} notas(s) de 100$")
if notas_50 > 0:
    print(f"{notas_50} notas(s) de 50$") 
if notas_20 > 0:
    print(f"{notas_20} notas(s) de 20$") 
if notas_10 > 0:
    print(f"{notas_10} notas(s) de 10$") 
if notas_5 > 0:
    print(f"{notas_5} notas(s) de 5$") 
if notas_2 > 0:
    print(f"{notas_2} notas(s) de 2$") 

