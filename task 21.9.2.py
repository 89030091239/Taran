class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


rect = Rectangle(10, 20)
print(rect.get_area())