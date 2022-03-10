vel = int(input("Velocidade do carro: \n"))
if vel > 80:
    print("Você está acima do limite permitido! \n velocidade de {}km/h!".format(vel))
    multa = 7 * (vel - 80)
    print("Sua multa é de R${:.2f}.".format(multa))
else:
    print("Velocidade dentro do limite. Boa viagem.")
