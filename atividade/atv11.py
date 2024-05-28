# Questão 11
# Desconto
while True:
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break

    print('Digite o preço do produto: ')
    pre = float(input())

    print('Digite o valor do desconto a ser aplicado: ')
    des = float(input())

    #Resultado
    soma = (pre - (pre * des/100))
    if soma:
        print('O valor do produto final foi de: ' + str(soma))