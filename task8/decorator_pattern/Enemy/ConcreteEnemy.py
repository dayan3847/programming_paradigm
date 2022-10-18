from abc import ABC

from Enemy.Enemy import Enemy


class ConcreteEnemy(Enemy, ABC):

    def compute_who_am_i(self):
        print("I AM NAKED")

