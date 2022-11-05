import queue
import threading


class Hilo3(threading.Thread):

    def __init__(self, q, valor_1, valor_2):
        threading.Thread.__init__(self, name="Hilo_3", target=Hilo3.calcular_frentes, args=(self, q, valor_1, valor_2))

    def calcular_frentes(self, q: queue.Queue, valor_1, valor_2):
        q.put_nowait(valor_1 * valor_2 * 2)
        print("Se ejecutó: calcular frentes")

