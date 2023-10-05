numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))

if numero < 1 or numero > 10:
    print("Número fora do intervalo válido.")
else:
    print(f"Tabuada do {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
