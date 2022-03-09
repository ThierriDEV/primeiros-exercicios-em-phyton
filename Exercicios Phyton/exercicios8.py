print('\t ----- Contando os Dígitos ----- ')

digitos = int(
    input("Digite um numero para que façamos a contagem dos dígitos: "))
contador = 0

while digitos != 0:
    digitos //= 10
    contador += 1

print("Total de dígitos = ", contador)
