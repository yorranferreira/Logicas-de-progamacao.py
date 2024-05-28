# Questão 6
#Número
while True:
    #fechar programa
    encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
    if encerrar == 'x':
      print("Programa encerrado.")
      break
    print('Digite um número: ')
    n1 = int(input())
    print('Digite um número: ')
    n2 = int(input())
    print('Digite um número: ')
    n3 = int(input())

    # Identifica quem é o maior
    if n1 == n2 and n2 == n3 :
        print(n1 , n2 , ' e ' , n3 , ' são o mesmo número.')
    elif n1 > n2 and n3 :
        print('O maior número é: ' , n1)
    elif n2 > n1 and  n3 :
        print('O maior número é: ' , n2)
    elif n3 > n1 and  n2 :
        print('O maior número é: ' , n3)
