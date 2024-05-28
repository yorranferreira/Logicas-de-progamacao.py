# Questão 10
# Triângulo
while True:
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break
    
    print('Numere o primeiro lado: ')
    l1 = float(input())
    print('Numere o segundo lado: ')
    l2 = float(input())
    print('Numere o terceiro lado: ')
    l3 = float(input())

    #testar os lados
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        if l1==l2==l3:
            print('Equilátero')
        elif l1!=l2 and l2!=l3 and l3!=l1:
            print('Escaleno')
        else:
            print('Isósceles')
    else:
        print('os lados não se constitui triângulo')