import pytest
from src.Square import Square
from constants import Data


def test_square_area_positive():
    s = Square(Data.SQUARE_SIDE)
    assert s.get_area() == 81


def test_square_perimetr_positive():
    s = Square(Data.SQUARE_SIDE)
    assert s.get_perimetr() == 36


@pytest.mark.parametrize('side_a', [0, -1])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
