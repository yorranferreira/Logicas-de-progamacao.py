while True:
    qtd_numeros = input("Digite a quantidade de números que você deseja verificar (digite 'x' para encerrar): ")

    if qtd_numeros == 'x':
        print("Programa encerrado.")
        break

    qtd_numeros = int(qtd_numeros)

    for _ in range(qtd_numeros):
        numero = int(input("Digite o número: "))

        if numero % 2 == 0:
            print("O número", numero, "é par.")
        else:
            print("O número", numero, "é ímpar.")
