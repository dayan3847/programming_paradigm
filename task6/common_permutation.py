def common_permutation(palabra_1, palabra_2):
    resultado = []
    recorrer = ""
    comparar = ""
    if len(palabra_1) < len(palabra_2):
        recorrer = palabra_1
        comparar = palabra_2
    else:
        recorrer = palabra_2
        comparar = palabra_1

    for temp in recorrer:
        if temp not in resultado:
            cantidad_recorrer = recorrer.count(temp)
            cantidad_comparar = comparar.count(temp)

            if cantidad_recorrer == cantidad_comparar or cantidad_recorrer < cantidad_comparar:
                for b in range(cantidad_recorrer):
                    resultado.append(temp)


            elif cantidad_recorrer > cantidad_comparar:
                for b in range(cantidad_comparar):
                    resultado.append(temp)

            else:
                for b in range(cantidad_recorrer):
                    resultado.append(temp)

    return resultado



if __name__ == '__main__':

    entradas = []
    mostrar_menu = True
    while mostrar_menu:

        print("1. Añadir pareja de palabras.")
        print("2. Continuar con el programa")

        eleccion = input("Seleccione una opcion.")

        if eleccion == "1":
            pareja_palabras = []
            for a in range(2):
                palabra = input("Escriba un string: ")
                palabra = palabra.replace(" ", "")
                palabra = palabra.lower()
                pareja_palabras.append(palabra)

            entradas.append(pareja_palabras)

        elif eleccion == "2":
            mostrar_menu = False
            for a in entradas:
                print(common_permutation(a[0], a[1]))

