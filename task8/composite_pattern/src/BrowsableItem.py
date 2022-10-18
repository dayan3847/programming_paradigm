from abc import ABC, abstractmethod
from typing import List


class BrowsableItem(ABC):
    _name: str

    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def show(self, parent_name: str = '') -> List[str]:
        pass
