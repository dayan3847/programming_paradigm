from typing import List

from BrowsableItem import BrowsableItem


class Directory(BrowsableItem):
    sub_items: List[BrowsableItem]

    def __init__(self, name: str):
        super().__init__(name)
        self.sub_items = []

    def show(self, parent_name: str = '') -> List[str]:
        result: List[str] = [parent_name + self._name + '/']
        for item in self.sub_items:
            result += item.show(parent_name + self._name + '/')
        return result

    def add_item(self, item: BrowsableItem) -> bool:
        self.sub_items.append(item)
        return True
