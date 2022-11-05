import queue
import time

from AreaBases import Hilo1
from AreaFrentes import Hilo3
from AreaLados import Hilo2

if __name__ == '__main__':
    print("Entre las dimensiones del prisma para calcular su area total.")
    print("Entre las dimensiones de la base y luego la altura.")

    lado_1 = int(input("Primer lado de la base: "))
    lado_2 = int(input("Segundo lado de la base: "))
    lado_3 = int(input("Altura del prisma: "))

    tiempo_inicio = time.time()
    q = queue.Queue()

    h1 = Hilo1(q, lado_1, lado_2)
    h2 = Hilo2(q, lado_1, lado_3)
    h3 = Hilo3(q, lado_2, lado_3)

    h1.start()
    h2.start()
    h3.start()

    h1.join()
    h2.join()

    resultado_1 = q.get_nowait()
    resultado_2 = q.get_nowait()

    area_lateral = resultado_1 + resultado_2
    print("El area lateral es: ", area_lateral)

    h3.join()

    resultado_3 = q.get_nowait()
    area_total = area_lateral + resultado_3

    tiempo_fin = time.time()
    print("El área total es: ", area_total)
    print("El programa se demoró: ", tiempo_fin - tiempo_inicio)
