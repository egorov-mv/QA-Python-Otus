import pytest
import requests

from api_tests.conftest import get_random_user_id_from_json
from api_tests.conftest import Const


def test_create():
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': '1'
    }
    r = requests.post(Const.BASE_URL_JSON + Const.POSTS, data=data)
    data.update({'id': 101})
    assert r.json() == data


@pytest.mark.parametrize('user_id', get_random_user_id_from_json(2))
def test_get_post(user_id):
    r = requests.get(Const.BASE_URL_JSON + Const.POSTS + '?userId=' + str(user_id))
    assert r.json()[0]['userId'] == user_id


@pytest.mark.parametrize('user_id', get_random_user_id_from_json(2))
def test_get_todos(user_id):
    r = requests.get(Const.BASE_URL_JSON + Const.USERS + '/' + str(user_id) + Const.TODOS)
    assert r.json()[0]['userId'] == user_id


def test_delete():
    r = requests.delete(Const.BASE_URL_JSON + Const.POSTS + '/1')
    assert r.status_code == Const.STATUS_CODE_OK


def test_patch():
    r = requests.patch(Const.BASE_URL_JSON + Const.POSTS + '/1', data={'title': 'foo'})
    assert r.json()['title'] == 'foo'
