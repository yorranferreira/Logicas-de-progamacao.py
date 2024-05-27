contador_impares = 0
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
    contador_impares += 1

    for numero_impar in range(numero + 2, numero + 12, 2):
        print("Próximo número ímpar:", numero_impar)
        contador_impares += 1
        
        if contador_impares == 5:
            break