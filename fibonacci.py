def instrucciones():
    primer_numero = 0
    numero_tope = int(input("dime el numero tope: "))
    return primer_numero, numero_tope


def main():
    primer_numero, numero_tope = instrucciones()
    lista = [primer_numero, 1]

    while lista[-1] + lista[-2] <= numero_tope:
        lista.append(lista[-1] + lista[-2])

    print(lista)
    
    exit()


main()
