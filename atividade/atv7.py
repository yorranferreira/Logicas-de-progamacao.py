# Questão 7
while True:
        #fechar programa
        encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
        if encerrar == 'x':
                print("Programa encerrado.")
                break
        print("Qual é o seu peso? ")
        p1 = float(input())
        print("Qual é a sua altura? ")
        p2 = float(input())

        #IMC
        imc = p1 / (p2 ** 2)
        if imc < 18.5:
                print("Você está Desnutrido", str (imc))
        elif 18.5 <= imc < 25:
                print("Você está com Peso adequado", str (imc))
        elif 25 <= imc < 30:
                print("Você está Sobrepeso", str (imc))
        else:
                print("Você está Obeso", str (imc))