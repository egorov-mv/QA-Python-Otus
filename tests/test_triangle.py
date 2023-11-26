import pytest
from src.Triangle import Triangle
from constants import Data


def test_triangle_area_positive():
    t = Triangle(Data.TRIANGLE_SIDE_A, Data.TRIANGLE_SIDE_B, Data.TRIANGLE_SIDE_C)
    assert round(t.get_area(), 2) == 81.39


def test_triangle_perimetr_positive():
    t = Triangle(Data.TRIANGLE_SIDE_A, Data.TRIANGLE_SIDE_B, Data.TRIANGLE_SIDE_C)
    assert t.get_perimetr() == 46


def test_circle_negative():
    with pytest.raises(ValueError):
        Triangle(Data.TRIANGLE_SIDE_A, Data.TRIANGLE_SIDE_B, Data.TRIANGLE_SIDE_WRONG)
