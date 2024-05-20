#!/usr/bin/python3
"""Takes in the ID, sends a request and displays response."""


import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    u_id = sys.argv[1]
    name = requests.get(url + "{}".format(u_id)).json().get('name')
    todos = requests.get(url + "{}/todos".format(u_id)).json()

    tasks = len(todos)
    done = []
    for i in todos:
        if i['completed']:
            done.append(i['title'])

    print('Employee {} is done with tasks({}/{}):'.format(
                                                          name,
                                                          len(done),
                                                          tasks))
    for i in done:
        print('\t {}'.format(i))
