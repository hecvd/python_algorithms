from __future__ import division
from datetime import datetime

PRIORITY_HIGH = 2
PRIORITY_MIDDLE = 1
PRIORITY_LOW = 0


class PriorityTask(object):

    def __init__(self, priority=PRIORITY_MIDDLE, timestamp=None):
        # self.index = index
        self.priority = priority
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp

    # def object_check(func):
    #     def wrap(self, other):
    #         if isinstance(other, PriorityTask):
    #             other = other.index
    #         return func(self, other)
    #     return wrap

    def __cmp__(self, other):
        if self.priority == other.priority:
            if self.timestamp == other.timestamp:
                return 0
            elif self.timestamp > other.timestamp:
                return -1
            else:
                return 1
        elif self.priority < other.priority:
            return -1
        elif self.priority > other.priority:
            return 1

    # def __div__(self, other):
    #     return self.__truediv__(other)
    #
    # @object_check
    # def __truediv__(self, other):
    #     return self.index / other
    #
    # @object_check
    # def __floordiv__(self, other):
    #     return self.index // other
    #
    # @object_check
    # def __mul__(self, other):
    #     return self.index * other
    #
    # @object_check
    # def __add__(self, other):
    #     return self.index + other

    def __str__(self):
        return 'Priority: %s Timestamp: %s' % (self.priority, self.timestamp)

    def __repr__(self):
        return str(self)

    # object_check = staticmethod(object_check)
