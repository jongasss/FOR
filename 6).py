n = int(input("Quantos números deseja inserir? "))

numero = float(input("Digite o primeiro número: "))
menor_valor = numero
maior_valor = numero
soma = numero

for i in range(1, n):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

    if numero < menor_valor:
        menor_valor = numero
    elif numero > maior_valor:
        maior_valor = numero

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma}")
