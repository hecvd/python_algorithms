from __future__ import division, print_function
from priority_task import PriorityTask
from datetime import datetime, timedelta
import random


class PriorityList:

    def __init__(self):
        self.heap_list = [PriorityTask(0)]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2

    def insert(self, priority, timestamp=None):
        self.heap_list.append(PriorityTask(priority, timestamp))
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def max_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_max(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [PriorityTask(0)]
        for item in alist:
            task = PriorityTask(*item)
            print('insert: {}'.format(str(task)))
            self.heap_list.append(task)
        while i > 0:
            self.perc_down(i)
            i -= 1

    def size(self):
        return self.current_size

pl = PriorityList()
pl.build([(a, datetime.utcnow() + timedelta(seconds=random.randint(0, 100))) for a in random.sample([0, 1, 2] * 5, 15)])

print()

while pl.size():
    print('get task: {}'.format(pl.del_max()))


