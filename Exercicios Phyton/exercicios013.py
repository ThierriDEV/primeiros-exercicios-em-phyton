largura = float(input("Digite a largura: \n"))
altura = float(input("Digite a Altura: \n"))
area = largura*altura


print("Sua parede tem a dimensão {} x {}, e a sua aréa é de {}m². " .format(
    largura, altura, area))

# CADA LITRO (L) DE TINTA PINTA UMA AREA DE 2m².
tinta_necessaria = area/2
print("Para pintar essa parede, você precisará de {}L de tinta." .format(
    tinta_necessaria))
