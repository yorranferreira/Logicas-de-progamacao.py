#Salário

print('Digite seu salário: ')
sal = float(input())

#Resultado
soma = (sal * (12/100)) + sal
if soma:
    print('O seu novo salário é: ' + str(soma))
