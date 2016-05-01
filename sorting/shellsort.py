import random


class ShellSort(object):

    def __call__(self, mlist):
        return self.shellsort(mlist)

    def shellsort(self, mlist):
        sublistcount = len(mlist) // 2
        while sublistcount > 0:
            for startposition in range(sublistcount):
                self._insertion_gap(mlist, startposition, sublistcount)
            sublistcount = sublistcount // 2
        return mlist

    def _insertion_gap(self, mlist, start, gap):
        for i in range(start + gap, len(mlist), gap):
            current = mlist[i]
            position = i
            while position >= gap and mlist[position - gap] > current:
                mlist[position] = mlist[position - gap]
                position = position - gap
            mlist[position] = current

shellsort = ShellSort()
print shellsort(random.sample(range(100), 10))

