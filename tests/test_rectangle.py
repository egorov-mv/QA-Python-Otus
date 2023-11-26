import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from constants import Data


@pytest.mark.parametrize(('rectangle_sides', 'area'),
                         [
                            ('integer', 30),
                            ('float', 33.39)
                         ], ids=['integer', 'float'])
def test_rectangle_area_positive(get_param_for_rectangle, rectangle_sides, area):
    side_a, side_b = get_param_for_rectangle(rectangle_sides=rectangle_sides)
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area


@pytest.mark.parametrize(('rectangle_sides', 'perimetr'),
                         [
                            ('integer', 22),
                            ('float', 23.2)
                         ], ids=['integer', 'float'])
def test_rectangle_perimetr_positive(get_param_for_rectangle, rectangle_sides, perimetr):
    side_a, side_b = get_param_for_rectangle(rectangle_sides=rectangle_sides)
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr() == perimetr


def test_add_area_positive():
    r = Rectangle(Data.RECTANGLE_SIDE_A, Data.RECTANGLE_SIDE_B)
    s = Square(Data.SQUARE_SIDE)
    assert r.add_area(s) == 96


@pytest.mark.parametrize(('side_a', 'side_b'),
                         [
                             (0, 1),
                             (1, 0),
                             (1, -1),
                             (-1, 1)
                         ])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_add_area_negative():
    r = Rectangle(Data.RECTANGLE_SIDE_A, Data.RECTANGLE_SIDE_B)
    const = Data.INT
    with pytest.raises(ValueError):
        r.add_area(another_figure=const)
