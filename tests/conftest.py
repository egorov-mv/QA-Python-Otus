import pytest


@pytest.fixture()
def get_param_for_rectangle():
    def _wrapper(rectangle_sides: str):
        if rectangle_sides == 'integer':
            return 5, 6
        elif rectangle_sides == 'float':
            return 5.3, 6.3
    yield _wrapper
