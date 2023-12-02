import json
import csv
import os

USERS_FILE_NAME = 'users.json'
BOOKS_FILE_NAME = 'books.csv'
RESULT_FILE_NAME = 'result.json'

def get_path (path_ending):
    base_path = os.getcwd()
    full_path = os.path.join(base_path, path_ending)
    return full_path


def get_books(path_ending):
    file_path = get_path(path_ending)
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        books = list(reader)
    result = [
        {
            'title': book['Title'],
            'author': book['Author'],
            'pages': int(book['Pages']),
            'genre': book['Genre']
        } for book in books
    ]
    return result


def get_users(path_ending):
    file_path = get_path(path_ending)
    with open(file_path, 'r') as file_json:
        users = json.load(file_json)
    result = [
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []
        } for user in users
    ]

    return result


def add_books_for_users(users, books):
    index = 0
    users_count = len(users)

    for book in books:
        user = users[index]
        user['books'].append(book)
        index = (index + 1) % users_count

    return users


def write_json(users_with_books, path_ending):
    file_path = get_path(path_ending)
    with open(file_path, "w") as writer:
        json.dump(users_with_books, writer, indent=4)


if __name__ == '__main__':
    books = get_books(BOOKS_FILE_NAME)
    users = get_users(USERS_FILE_NAME)
    users_with_book = add_books_for_users(users, books)
    write_json(users_with_book, RESULT_FILE_NAME)
