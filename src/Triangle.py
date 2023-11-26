from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name='Triangle')
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError('Нельзя создать треугольник с заданными значениями сторон')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        p = self.get_perimetr()/2
        return math.sqrt(p*(p - self.side_a)*(p - self.side_b)*(p - self.side_c))
