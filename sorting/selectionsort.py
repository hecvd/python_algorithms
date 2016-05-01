import random


class SelectionSort(object):

    def __init__(self):
        pass

    def __call__(self, mlist):
        return self.selection(mlist)

    @staticmethod
    def selection(mlist):
        if not mlist:
            return mlist
        print mlist
        for i in range(len(mlist)-1):
            indx = i
            for j in range(i+1, len(mlist)):
                if mlist[indx] > mlist[j]:
                    indx = j
            if indx != i:
                mlist[i], mlist[indx] = mlist[indx], mlist[i]

        return mlist

selectionsort = SelectionSort()
print selectionsort(random.sample(range(100), 10))




