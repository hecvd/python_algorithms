import random


class QuickSort(object):

    def __init__(self):
        pass

    def __call__(self, mlist):
        return self.quicksort(mlist, 0, len(mlist) - 1)

    @staticmethod
    def swap(mlist, i, j):
        tmp = mlist[i]
        mlist[i] = mlist[j]
        mlist[j] = tmp
    # ??
    # def best_pivot(self, mlist, st, en):
    #     mid = (st + en)//2
    #     if mlist[mid] > mlist[en]:
    #         self.swap(mlist, mid, en)
    #     if mlist[st] < mlist[mid]:
    #         if mlist[st] > mlist[en]:
    #             self.swap(mlist, st, en)
    #         else:
    #             self.swap(mlist, st, mid)

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
        # self.best_pivot(mlist, first, last)
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

import timeit


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

quicksort = QuickSort()
l = random.sample(range(100), 10)

print('Original: \t\t' + str(l))
print('Result: \t\t' + str(quicksort(l)))

