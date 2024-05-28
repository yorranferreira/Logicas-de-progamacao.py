
# Questão 4
# #Salário

while True:
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break

    print('Digite seu salário: ')
    sal = float(input())

    #Resultado
    soma = (sal * (12/100)) + sal
    if soma:
        print('O seu novo salário é: ' + str(soma))
