n = float(input("Digite o preço de um produto: \n"))
desconto = n*15/100
print("Na liquidação da loja, esse produto de R$ {:.2f} está com desconto de 15%, \n ou seja, vai custar apenas R${:.2f}." .format(
    n, n-desconto))
