import requests
import random


class Const:
    BASE_URL_DOG = 'https://dog.ceo/api'
    BASE_URL_JSON = 'https://jsonplaceholder.typicode.com'
    BREEDS = '/breeds'
    BREED = '/breed'
    LIST = '/list'
    ALL = '/all'
    USERS = '/users'
    IMAGES = '/images'
    RANDOM = '/random'
    IMAGE = '/image'
    STATUS_CODE_OK = 200
    SUCCESS = 'success'
    POSTS = '/posts'


def pytest_addoption(parser):
    parser.addoption("--url", default=" https://ya.ru")
    parser.addoption("--status_code", default=200)


def get_random_user_id(count):
    r = requests.get(Const.BASE_URL_JSON + Const.USERS)
    return random.sample([k['id'] for k in r.json()], count)


def get_all_breeds():
    r = requests.get(Const.BASE_URL_DOG + Const.BREEDS + Const.LIST + Const.ALL)
    return r.json()['message'].keys()


def get_all_sub_breeds():
    r = requests.get(Const.BASE_URL_DOG + Const.BREEDS + Const.LIST + Const.ALL)
    return {key : value for key, value in r.json()['message'].items() if value}
