class shape:
    def area(self):
        raise NotImplementedError
class circle(shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class rectangle(shape):
    def __init__(self, length, width):
        self.length =  length
        self.width = width
    def area(self):
        return self.length * self.width
        