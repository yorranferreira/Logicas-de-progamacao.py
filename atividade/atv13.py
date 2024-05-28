# Questão 13
# Troco
while True:
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break

    print('Digite o valor da compra: ')
    val = float(input())

    print('Digite o valor pago pelo cliente: ')
    cli = float(input())

    #Resultado
    soma = (cli - val)
    if soma:
      print('O troco é: ' + str(soma))