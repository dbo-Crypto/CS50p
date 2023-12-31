import emoji


class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"{self.size * emoji.emojize(':cookie:')}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Jar full")
        self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Jar empty")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Incorrect capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Incorrect size")
        self._size = size
