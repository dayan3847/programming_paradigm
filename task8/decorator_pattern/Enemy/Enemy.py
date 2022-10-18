from abc import ABC, abstractmethod


class Enemy(ABC):

    @abstractmethod
    def compute_who_am_i(self, received_attack):
        pass
