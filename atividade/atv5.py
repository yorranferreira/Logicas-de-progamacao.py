# Questão 5
# Idade
while True:
    
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break

    print('Digite sua idade: ')
    n = int(input())

    if n >= 18:
        print('Você é maior de idade')
    elif n < 18:
        print('Você é menor de idade!')