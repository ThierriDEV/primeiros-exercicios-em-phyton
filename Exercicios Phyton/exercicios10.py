print('\t ----- Conversor de Real R$ para Dólar US$ -----')

n = float(input("Quanto em Reais você tem? \nR$ "))
dolar = 5.26
conversao = n/dolar
print("Com R${} você pode comprar US${:.2f}." .format(n, conversao))
