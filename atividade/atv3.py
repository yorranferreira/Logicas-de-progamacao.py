# Questão 3
while True:
    qtd_numeros = input("Digite a quantidade de números que você deseja verificar (digite 'x' para encerrar): ")
    
    if qtd_numeros == 'x':
        print("Programa encerrado.")
        break
    qtd_numeros = int(qtd_numeros)
    
    for i in range(qtd_numeros):
        numero = float(input("Digite o número: "))
        
        if numero > 0:
            print("O número", numero, "é positivo.")
        elif numero < 0:
            print("O número", numero, "é negativo.")
        else:
            print("O número", numero, "é zero.")