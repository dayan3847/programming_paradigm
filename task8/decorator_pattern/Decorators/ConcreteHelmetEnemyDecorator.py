from abc import ABC

from Decorators.EnemyDecorator import EnemyDecorator


class ConcreteHelmetEnemyDecorator(EnemyDecorator, ABC):

    def compute_who_am_i(self):
        print("I HAVE HELMET")
        self.decorated_enemy.compute_who_am_i()
