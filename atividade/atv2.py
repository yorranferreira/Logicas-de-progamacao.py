# Questão 2
# Conversor de Unidades: Graus Celsius e Fahrenheit
while True:
   #fechar programa
   encerrar = input('Digite 0 para iniciar o programa, ou a tecla "X" para encerrar: ')
   if encerrar == 'x':
      print("Programa encerrado.")
      break
   
   print('Digite a temperatura em °C: ')
   tempC = float(input())

   #Converter o °C para °F
   tempF = (1.8*tempC) + 32
   print(' A temperatura correspondente a ' + str(tempF) + '°F')