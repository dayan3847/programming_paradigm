import queue
import threading
import time


class Hilo1(threading.Thread):

    def __init__(self, q, valor_1, valor_2):
        threading.Thread.__init__(self, name="Hilo_1", target=Hilo1.calcular_bases, args=(self, q, valor_1, valor_2))

    def calcular_bases(self, q: queue.Queue, valor_1, valor_2):
        time.sleep(1)
        q.put_nowait(valor_1 * valor_2 * 2)
        print("Se ejecutó: calcular base")

