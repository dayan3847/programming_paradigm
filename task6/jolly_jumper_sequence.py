def jolly_jumers(linea):

    if len(linea) == 1:
        print("Jolly")
    else:
        indica_cant = linea.pop(0)
        if indica_cant != len(linea):
            print("Not Jolly")
        else:
            is_jolly = True
            resultados = []
            i = 0

            while i < len(linea)-1 and is_jolly:
                resultado = abs(linea[i] - linea[i + 1])
                if resultado in resultados:
                    print("Not Jolly")
                    is_jolly = False
                elif resultado >= indica_cant:
                    print("Not Jolly")
                    is_jolly = False
                else:
                    resultados.append(resultado)
                    i += 1

            if is_jolly:
                print("Jolly")


if __name__ == '__main__':

    try:
        cantidad = int(input("Entre la cantidad de numeros: "))
        if cantidad < 3000:
            linea = []
            linea.append(cantidad)
            añadir = True
            while(añadir):
                valor = input("Entre un numero entero entre la letra n para continuar: ")
                if valor != "n":
                    linea.append(int(valor))
                else:
                    añadir = False
        else:
            print("la cantidad tiene que ser menor que 3000.")
    except:
        print("Solo debe introducir numeros enteros.")

    jolly_jumers(linea)

