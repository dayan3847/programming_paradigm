from abc import ABC, abstractmethod

from Enemy.Enemy import Enemy


class EnemyDecorator(Enemy, ABC):

    def __init__(self, enemy):
        self.decorated_enemy = enemy

    @abstractmethod
    def compute_who_am_i(self):
        pass
