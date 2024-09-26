class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)

    def delete(self):
        if self.get_size() == 0:
            return None
        if self.get_size() == 1:
            return self.storage.pop(0)
        else:
            ref = self.storage[0]
            self.storage[0] = self.storage.pop(self.get_size() - 1)
            return ref

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
