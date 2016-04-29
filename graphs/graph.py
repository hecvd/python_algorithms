
class a(object):
    aa = a.__class__

    def __init__(self):
        print self.aa

