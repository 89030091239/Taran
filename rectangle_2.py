from rectangle import Rectangle, Square, Circle
import math
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# print(rect_1.get_area())
# print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
# print(square_1.get_area_square(),
#       square_2.get_area_square())

circle = Circle(math.pi, 10)

figures = [rect_1, rect_2, square_1, square_2, circle]

for figure in figures:
      if isinstance(figure, Square):  # Функция isinstance, поддерживающая наследование, проверяет, является ли аргумент объекта экземпляром класса или экземпляром класса из кортежа, возвращает True, или — False.
            print(figure.get_area_square())
      elif isinstance(figure, Circle):
            print(f'Площадь круга: {round(figure.get_area_circle(), 2)}')
      else:
            print(figure.get_area())

