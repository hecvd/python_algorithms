import random


def insertionsort(nlist):
    for indx, value in enumerate(nlist):
        while indx and nlist[indx - 1] > value:
            nlist[indx] = nlist[indx - 1]
            indx -= 1
        nlist[indx] = value
    return nlist

mlist = random.sample(range(100), 10)

print mlist
print insertionsort(mlist)
