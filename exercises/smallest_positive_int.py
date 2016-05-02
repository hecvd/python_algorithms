from __future__ import print_function
import random


class SmallestPositive(object):

    def __call__(self, mlist):
        return self.find_number(mlist)

    def find_number(self, mlist):
        index = 0
        max = len(mlist)
        while index < max:
            if (mlist[index] > 0) and mlist[index] <= max and mlist[index] \
                    != mlist[mlist[index] - 1]:
                a, b = index, mlist[index] - 1
                mlist[a], mlist[b] = mlist[b], mlist[a]
            index += 1
        for i, token in enumerate(mlist):
            if token != i + 1:
                return i + 1
        return max + 1


find_number = SmallestPositive()
print(find_number(random.sample(range(-10, 50), random.randint(0, 50))))
