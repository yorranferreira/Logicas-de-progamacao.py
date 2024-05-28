# Questão 9
# Bebê, criança, adolescente, adulto e idoso
while True:
    
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break

    print('Digite sua idade: ')
    n = int(input())

    if n <= 2:
        print('Você é um bebê!')
    elif n >= 3 and n <= 12:
        print('Você é uma criança!')
    elif n >= 13 and n <= 17:
        print('Você é uma adolescente!')
    elif n >= 18 and n <= 64:
        print('Você é um adulto!')
    else:
        print('Você é um idoso!')