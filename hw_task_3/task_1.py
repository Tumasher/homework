
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimetr(self):
        return (self.height + self.width) * 2


rec_1 = rectangle(2, 3)


print(rec_1.area())
print(rec_1.perimetr())