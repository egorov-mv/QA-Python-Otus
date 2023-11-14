from Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Радиус не может быть меньше 0')
        self.pi = 3.14
        self.radius = radius

    def get_perimetr(self):
        return self.pi * 2 * self.radius

    def get_area(self):
        return self.pi * self.radius * self.radius
