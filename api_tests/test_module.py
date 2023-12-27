import pytest
import requests


@pytest.fixture
def config(request):
    return [request.config.getoption("--url"), request.config.getoption("--status_code")]


def test_status(config):
    assert requests.get(config[0]).status_code == config[1]
