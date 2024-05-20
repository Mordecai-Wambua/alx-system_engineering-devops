#!/usr/bin/python3
"""Takes in the ID, sends a request and displays response."""


import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    names = requests.get(url + "/users").json()
    todos = requests.get(url + "/todos").json()

    data = {}
    for name in names:
        for i in todos:
            if i['userId'] == name['id']:
                data.update({i['id']: [{
                    "username": name['username'],
                    "task": i['title'],
                    "completed": i['completed']}]})

    filename = 'todo_all_employees.json'

    with open(filename, mode='w') as file:
        json.dump(data, file)
