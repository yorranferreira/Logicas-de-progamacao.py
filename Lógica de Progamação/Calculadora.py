#calculadora

#entrada de dados
print('Digite o primeiro número: ')
n1 = float(input())
print('Digite o segundo número: ')
n2 = float(input())

#selecione a operação
print('Escolha a operação: ')
print('1 - adição')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
op = int(input())

#análise da opção escolhida
if op == 1:
    result = n1 + n2
    print('resultado: ' + str(result))
elif op == 2:
    result = n1 - n2
    print('resultado: ' + str(result))
elif op == 3:
    result = n1 * n2
    print('resultado: ' + str(result))
elif op == 4:
    result = n1 / n2
    print('resultado: ' + str(result))
else:
    print('opção inválida!')