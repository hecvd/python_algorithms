class Node(object):
  
  def __init__(self, value):
    self.value = value
    self.nxt = None
    self.prev = None


class LinkedList(object):
  
  def __init__(self):
    self.head = None
  
  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.nxt

  def __str__(self):
    return " -> ".join(map(str, (i.value for i in self)))
  
  def __repr__(self):
    return " -> ".join(map(str, (i.value for i in self)))
  
  def append_left(self, value):
    node = Node(value)
    node.nxt = self.head
    self.head = node

  def append_right(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      nxt = self.head
      while nxt.nxt:
        nxt = nxt.nxt
      nxt.nxt = Node(value)

  def delete_node(self, node):
    pass
  
  def pop_right(self):
    if not self.head:
      return
    if not self.head.nxt:
      self.head = None
      return
    node = self.head
    while node.nxt and node.nxt.nxt:
      node = node.nxt
    node.nxt = None

  def pop_left(self):
    self.head = self.head.nxt


class DoubleLinkedList(object):
  pass



