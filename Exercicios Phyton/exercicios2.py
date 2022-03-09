print('----------- TABUADA ----------')
numero = int(input('Informe um numero para ver a tabuada: '))

print('\n Tabuada de', numero, ':')


for i in range(1, 11):
    print(numero, ' X ', i, '=', (numero * i))
