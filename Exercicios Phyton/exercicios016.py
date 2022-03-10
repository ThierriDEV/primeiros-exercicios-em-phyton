dias = int(input("Por quantos dias o carro foi alugado: \n"))  # 8 didas
km = float(input("Quantos km o carro rodou: \n"))  # 720km

custo_dias = (dias*60)
custo_km = (km*0.15)

print("Você andou {}km por {} dias, então o preço a pagar é R${:.2f}." .format(
    km, dias, (custo_km+custo_dias)))

# TEM QUE DAR COMO RESULTADO R$588,00
