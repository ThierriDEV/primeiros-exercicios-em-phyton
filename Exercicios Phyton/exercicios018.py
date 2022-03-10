dist = int(input("Qual a distância a ser percorrida? \n"))
if dist <= 200:
    price = (dist * 0.50)
print("Preço da passagem: R${:.2f}." .format(price))
price = (dist * 0.45)
print("Preço da passagem: R${:.2f}." .format(price))
