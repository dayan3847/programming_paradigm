from typing import List

from BrowsableItem import BrowsableItem


class File(BrowsableItem):

    def show(self, parent_name: str = '') -> List[str]:
        return [parent_name + self._name]
