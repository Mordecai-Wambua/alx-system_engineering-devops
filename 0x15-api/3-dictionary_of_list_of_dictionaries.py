#!/usr/bin/python3
"""Takes in the ID, sends a request and displays response."""


import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + "/users").json()
    todos = requests.get(url + "/todos").json()

    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        data[user_id] = []
        for i in todos:
            if i['userId'] == user_id:
                data[user_id].append({
                    "username": username,
                    "task": i['title'],
                    "completed": i['completed']})

    filename = 'todo_all_employees.json'

    with open(filename, mode='w') as file:
        json.dump(data, file)
