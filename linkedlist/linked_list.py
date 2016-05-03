from node import Node


class LinkedList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return not self._head

    def _add_first(self, item):
        if self.is_empty():
            self._head = item
            return True
        return False

    @Node.make_node
    def add(self, item):
        if not self._add_first(item):
            item.next_node = self._head
            self._head = item
        return self

    @Node.make_node
    def add_right(self, item):
        return
        # if self._add_first(item):
        #     return

    def size(self):
        return sum(1 for i in self)

    def search(self, value):
        return any(elem for elem in self if elem == value)

    def remove(self, value):
        # nodes = [t for t in self.iternodes(True) if t.value == value]
        if self.is_empty():
            return
        found = False
        current = self._head
        previous = None
        while not found and current:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next_node
        if previous is None:
            self._head = current.next_node
        else:
            previous.next_node = current.next_node

    def __iter__(self):
        return self.iternodes()

    def iternodes(self, nodes=False):
        current = self._head
        while current:
            yield current if nodes else current.value
            current = current.next_node

    def __str__(self):
        return str(' '.join(str(t) for t in self))

    def __len__(self):
        return sum(1 for i in self)

    def __getitem__(self, item):
        current = self._head
        size = self.size()
        if not size or item >= size:
            raise IndexError
        while item > 0:
            current = current.next_node
            item -= 1
        return current.value
