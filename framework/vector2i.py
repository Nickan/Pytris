class Vector2i(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def set(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, x=0, y=0):
        self.x + x
        self.y + y

    def inc(self, vector):
        self.x += vector.x
        self.y += vector.y
