import pytest
from src.Circle import Circle
from constants import Data


def test_circle_area_positive():
    c = Circle(Data.CIRCLE_RADIUS)
    assert c.get_area() == 153.86


def test_circle_perimetr_positive():
    c = Circle(Data.CIRCLE_RADIUS)
    assert c.get_perimetr() == 43.96


@pytest.mark.parametrize('radius', [0, -1])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
