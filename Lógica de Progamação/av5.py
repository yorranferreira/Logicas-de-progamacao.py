numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

menor_numero = numero1

if numero2 < menor_numero:
    menor_numero = numero2
if numero3 < menor_numero:
    menor_numero = numero3

print("O menor número digitado é:", menor_numero)

for i in range(1, menor_numero + 1):
    print("Número:", i, "- Par" if i % 2 == 0 else "- Ímpar")