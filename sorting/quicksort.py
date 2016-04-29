class QuickSort(object):

    def __init__(self):
        pass

    def __call__(self, mlist):
        return self.quicksort(mlist, 0, len(mlist) - 1)

    def _median(self, a, b, c):
        if (a - b) * (b - c) > -1:
            return b
        elif (a - b) * (a - c) < 1 :
            return a
        else:
            return c

    def quicksort(self, mlist, st, en):
        if st > en:
            return mlist
        pivot = self._median(mlist[st], mlist[en], mlist[(st + en)//2])
        self._partition(mlist, pivot, st, en)

    def _partition(self, mlist, pivot, st, en):
        value = mlist[pivot]
        while st < en:
            if st != pivot or en != pivot:
                continue
            if mlist[st] > mlist[en]:
                pass

