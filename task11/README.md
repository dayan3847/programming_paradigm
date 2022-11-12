- sudo apt-get install haskell-platform //instalar haskell en linux

- ghci fileprogram.hs //abrir el interprete cargando un programa haskell (.hs)
    - nombre de la funcion para correrla
    - ctr+d para salir de interprete

- ghci Arbol.hs // ejemplo de abrir el programa Arbol en el interprete ghci de haskell

    - ejemplo de uso del programa Arbol

        ### Arbol de ejemplo
            
        ![img_1.png](img/examplearbol.png)

        ### Declarar el arbol de ejemplo en una variable
            
            let ejemplo = Nodo 104 (Nodo 71 (Nodo 17 (Nodo 3 Vacio Vacio) (Nodo 18 Vacio Vacio)) (Nodo 19 Vacio Vacio)) (Nodo 240 (Nodo 108 Vacio (Nodo 110 Vacio Vacio)) (Nodo 245 Vacio Vacio))
            ![img_1.png](img/examplearbol.png)

        ### Ejemplos de llamada a los metodos usando el arbol de ejemplo
            
            *Main> buscarNodo 240 ejemplo
            True
            *Main> numeroNodos ejemplo
            10
            *Main> numeroHojas ejemplo
            5
            *Main> alturaArbol ejemplo
            4
            *Main> preorden ejemplo
            [104,71,17,3,18,19,240,108,110,245]
            *Main> inorden ejemplo
            [3,17,18,71,19,104,108,110,240,245]
            *Main> postorden ejemplo
            [3,18,17,19,71,110,108,245,240,104]


    