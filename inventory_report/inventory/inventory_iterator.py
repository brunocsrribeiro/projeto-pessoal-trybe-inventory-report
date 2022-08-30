from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory_report):
        self.inventory_report = inventory_report
        self._index = 0

    def __next__(self):
        try:
            current_value = self.inventory_report[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return current_value
