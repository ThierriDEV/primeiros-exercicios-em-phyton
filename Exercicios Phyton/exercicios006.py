from re import I


somador = 0

numero = int(input("Por favor, Digite um numero: "))
for i in range(1, numero + 1, 1):
    somador += i
print("A soma dos numeros é = ", somador)
