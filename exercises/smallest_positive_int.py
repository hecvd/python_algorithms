from __future__ import print_function
import random


class SmallestPositive(object):

    def __call__(self, mlist):
        return self.find_number(mlist)

    def find_number(self, mlist):
        index = 0
        max = len(mlist)
        while index < max:
            if (mlist[index] > 0) and mlist[index] <= max and mlist[index] != mlist[mlist[index] - 1]:
                a, b = index, mlist[index] - 1
                mlist[a], mlist[b] = mlist[b], mlist[a]
            index += 1
        for i, token in enumerate(mlist):
            if token != i + 1:
                return i + 1
        return max + 1


    # def find_number(self, mlist):
    #     mlist = sorted(set(map(abs, mlist)))
    #     index = 0
    #     print(mlist)
    #     if not mlist:
    #         return 'empty list'
    #     if len(mlist) == 1:
    #         return mlist[0] - 1 if mlist[0] > 0 else mlist[0] + 1
    #     while index < len(mlist)-1:
    #         if mlist[index] > 1 and mlist[index] - 1 != mlist[index - 1]:
    #             return mlist[index] - 1
    #         if mlist[index] + 1 == mlist[index + 1]:
    #             index += 1
    #             continue
    #         break
    #     return mlist[index] + 1

find_number = SmallestPositive()
print(find_number(random.sample(range(-10, 50), random.randint(0, 50))))
