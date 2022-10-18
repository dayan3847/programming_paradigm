from Decorators.ConcreteArmourEnemyDecorator import ConcreteArmourEnemyDecorator
from Enemy.ConcreteEnemy import ConcreteEnemy
from Decorators.ConcreteHelmetEnemyDecorator import ConcreteHelmetEnemyDecorator

if __name__ == '__main__':

    """Creando un enemigo sin ningún decorador"""
    concrete_enemy = ConcreteEnemy()

    """Añadiendo un decorador de armadura al enemigo"""
    armour_enemy = ConcreteArmourEnemyDecorator(concrete_enemy)

    """Añadiendo un decorador de casco al enemigo"""
    helmet_armour_enemy = ConcreteHelmetEnemyDecorator(armour_enemy)

    """Ejecutando la función de identificación"""
    helmet_armour_enemy.compute_who_am_i()
