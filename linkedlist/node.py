class Node(object):

    def __init__(self, value, parent=None, child=None):
        self._next = child
        self._data = value
        self._parent = parent

    @staticmethod
    def make_node(func):
        def inner(self, value):
            value = Node(value)
            return func(self, value)
        return inner

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, node):
        self._next = node

    @property
    def prev_node(self):
        return self._parent

    @prev_node.setter
    def prev_node(self, node):
        self._parent = node

    @property
    def value(self):
        return self._data

    @value.setter
    def value(self, val):
        self._data = val
