from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError('Сторона квадрата не может быть меньше или равна 0')
        super().__init__(side_a, side_a)
