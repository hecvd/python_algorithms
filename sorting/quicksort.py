import random


class QuickSort(object):

    def __init__(self):
        pass

    def __call__(self, mlist):
        return self.quicksort(mlist, 0, len(mlist) - 1)

    def swap(self, mlist, i, j):
        tmp = mlist[i]
        mlist[i] = mlist[j]
        mlist[j] = tmp

    def quicksort(self, mlist, first, last):
        if first < last:
            index = self._partition(mlist, first, last)

            self.quicksort(mlist, first, index - 1)
            self.quicksort(mlist, index + 1, last)
        return mlist

    def _partition(self, mlist, first, last):
        left = first + 1
        right = last
        done = False
        pivot = mlist[first]
        while not done:
            while left <= right and mlist[left] <= pivot:
                left += 1
            while right >= left and mlist[right] >= pivot:
                right -= 1
            if right < left:
                done = True
            else:
                self.swap(mlist, left, right)
        self.swap(mlist, first, right)
        return right

quicksort = QuickSort()
l = random.sample(range(100), 10)
print quicksort(l)
