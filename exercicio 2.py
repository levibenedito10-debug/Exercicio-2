def contar_primos(lista, valor):
    contador = 0


    for primo in lista:
        if primo < valor:
            contador += 1
        else:
            break