import random
from itertools import islice
from collections import deque


class MergeSort(object):

    def __init__(self):
        pass

    def __call__(self, mlist):
        return self.mergesort(mlist)

    def mergesort(self, mlist):
        if len(mlist) <= 1:
            return mlist

        pivot = len(mlist) / 2
        leftlist = deque(islice(iter(mlist), 0, pivot))
        rightlist = deque(islice(iter(mlist), pivot, len(mlist)))
        leftlist = self.mergesort(leftlist)
        rightlist = self.mergesort(rightlist)

        return self._merge(leftlist, rightlist)

    def _merge(self, leftlist, rightlist):
        resplist = deque()
        while leftlist and rightlist:
            if leftlist[0] < rightlist[0]:
                resplist.append(leftlist.popleft())
            else:
                resplist.append(rightlist.popleft())
        while leftlist:
            resplist.append(leftlist.popleft())
        while rightlist:
            resplist.append(rightlist.popleft())
        return resplist


mergesort = MergeSort()
print mergesort(deque(random.sample(range(100000000), 1000)))


