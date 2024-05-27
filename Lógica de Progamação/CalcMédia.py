#Calcule a média entre 3 notas
#Verifica situação (aprovado ou reprovado)

#Entrada de notas pelo usuário
print('Digite a primeira nota e pressione ENTER: ')
n1 = int(input())
print('Digite a segunda nota e pressione ENTER: ')
n2 = int(input())
print('Digite a terceira nota e pressione ENTER: ')
n3 = int(input())

# Calcula a média
media = (n1 + n2 + n3)/3
if media >= 7:
    print('Aprovado! Sua média final foi: ' + str(media))
else:
    print('Reprovado! Sua média final foi: ' + str(media))
