import pytest
import requests
from api_tests.conftest import get_all_breeds
from api_tests.conftest import get_all_sub_breeds
from api_tests.conftest import Const
import random


@pytest.mark.parametrize('breed', get_all_breeds())
def test_get_images_by_breeds(breed):
    r = requests.get(Const.BASE_URL_DOG + Const.BREED + f'/{breed}' + Const.IMAGES + Const.RANDOM)
    assert r.status_code == Const.STATUS_CODE_OK
    assert r.json()['status'] == Const.SUCCESS
    assert '.jpg' in r.json()['message']


def test_get_random_images():
    r = requests.get(Const.BASE_URL_DOG + Const.BREEDS + Const.IMAGE + Const.RANDOM)
    assert r.status_code == Const.STATUS_CODE_OK
    assert r.json()['status'] == Const.SUCCESS
    assert '.jpg' in r.json()['message']

@pytest.mark.parametrize(('bread', 'sub_bread'), [(key, value) for key, value in get_all_sub_breeds().items()])
def test_get_sub_breed(bread, sub_bread):
    r = requests.get(Const.BASE_URL_DOG + Const.BREED+ f'/{bread}' + Const.LIST)
    assert r.json()['message'] == sub_bread
    assert r.status_code == Const.STATUS_CODE_OK


def test_test_get_random_sub_breed_images():
    bread, sub_bread = random.choice(list(get_all_sub_breeds().items()))
    r = requests.get(Const.BASE_URL_DOG+ Const.BREED+ f'/{bread}'+ f'/{sub_bread[0]}' + Const.IMAGES + Const.RANDOM)
    assert r.status_code == Const.STATUS_CODE_OK
