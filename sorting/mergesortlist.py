import random
from timeit import Timer


class MergeSort(object):

    def __init__(self):
        pass

    def __call__(self, mlist):
        return self.mergesort(mlist)

    def mergesort(self, mlist):
        if len(mlist) <= 1:
            return mlist

        pivot = len(mlist) / 2
        leftlist = self.mergesort(mlist[:pivot])
        rightlist = self.mergesort(mlist[pivot:])

        return self._merge(leftlist, rightlist)

    def _merge(self, leftlist, rightlist):
        resplist = []
        while leftlist and rightlist:
            if leftlist[0] < rightlist[0]:
                resplist.append(leftlist.pop(0))
            else:
                resplist.append(rightlist.pop(0))
        while leftlist:
            resplist.append(leftlist.pop(0))
        while rightlist:
            resplist.append(rightlist.pop(0))
        return resplist

mergesort = MergeSort()

t = Timer(lambda: mergesort(random.sample(xrange(100000000), 1000))).repeat(1000)
print t.timeit(number=1)
