
def memoize(func):
    mem = {}

    def inner(self, value):
        if value not in mem:
            mem[value] = func(self, value)
        return mem[value]

    return inner


class Fibonacci(object):

    def __init__(self):
        pass

    def generator(self, n):
        a, b = 1, 1

        for _ in range(n - 1):
            a, b = b, a + b
            yield a

    @memoize
    def non_recursive(self, n):
        a, b = 1, 1

        for _ in range(n-1):
            a, b = b, a + b

        return a

    @memoize
    def recursive(self, n):
        if n == 1 or n == 2:
            return 1
        print n
        return self.recursive(n - 1) + self.recursive(n - 2)
