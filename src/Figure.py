from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, new_figure):
        if not isinstance(new_figure, Figure):
            raise ValueError('Не фигура')
        return self.get_area() + new_figure.get_area()
