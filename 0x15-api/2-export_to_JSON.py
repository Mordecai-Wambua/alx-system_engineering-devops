#!/usr/bin/python3
"""Takes in the ID, sends a request and displays response."""


import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    u_id = sys.argv[1]
    name = requests.get(url + "{}".format(u_id)).json().get('username')
    todos = requests.get(url + "{}/todos".format(u_id)).json()

    data = {}
    data.update({u_id: [{
        "task": i['title'], "completed": i['completed'], "username": name}
        for i in todos]})

    print(data)

    filename = f'{u_id}.json'

    with open(filename, mode='w') as file:
        json.dump(data, file)
