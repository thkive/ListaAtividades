c = 0 
primos = 0

for c in range(2, 101):
    eh_primo = True
    for i in range(2, c):
        if c % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(c, end=", ")
        primos += 1
print(f"\nO total de numeros primos é: {primos}")
