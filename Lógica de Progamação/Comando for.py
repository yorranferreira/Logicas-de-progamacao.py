#vetor
while(1):
    numero = []
    for x in range(4):
        print('Digite o nº desejado: ')  
        
        num = float(input())
        numero.append(num)
  
        if num == 0:
            print("Número 0 digitado, saindo do loop.")
            break
    print('você digitou os nº: ', numero)