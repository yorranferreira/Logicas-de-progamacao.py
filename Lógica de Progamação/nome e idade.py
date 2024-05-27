#Nome e idade
print('Qual seu nome? ')
n1 = str(input())
print('Qual sua idade? ')
id1 = int(input())
print('Qual seu nome? ')
n2 = str(input())
print('Qual sua idade? ')
id2 = int(input())

# Identifica quem é o mais velho
if id1 > id2 :
    print('O(a) mais velho(a) é ' + n1 + " com a idade de " + str(id1) + ' anos.') 
elif id1 < id2 :
    print('O(a) mais velho(a) é ' + n2 + " com a idade de " + str(id2) + ' anos.') 
else:
    print(n1 + ' e ' + n2 + " tem a mesma idade com " + str(id2) + ' anos.')