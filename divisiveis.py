numeros_encontrados = 0
numero_atual = 1

while numeros_encontrados < 20:
    if numero_atual % 2 == 0 and numero_atual % 5 == 0:
        print(numero_atual)
        numeros_encontrados += 1

    numero_atual += 1