import queue
import threading


class Hilo2(threading.Thread):

    def __init__(self, q, valor_1, valor_2):
        threading.Thread.__init__(self, name="Hilo_2", target=Hilo2.calcular_lados, args=(self, q, valor_1, valor_2))

    def calcular_lados(self, q: queue.Queue, valor_1, valor_2):
        q.put_nowait(valor_1 * valor_2 * 2)
        print("Se ejecutó: calcular lados")

