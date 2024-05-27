numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma_pares = 0

if numero1 < numero2:
    inicio = numero1
    fim = numero2
else:
    inicio = numero2
    fim = numero1

print("Números pares entre", inicio, "e", fim, ":")

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)
        soma_pares += numero

print("A soma dos números pares é:", soma_pares)