from abc import ABC

from Decorators.EnemyDecorator import EnemyDecorator


class ConcreteArmourEnemyDecorator(EnemyDecorator, ABC):

    def compute_who_am_i(self):
        print("I HAVE ARMOUR")
        self.decorated_enemy.compute_who_am_i()
