#!/usr/bin/python3
"""Takes in the ID, sends a request and displays response."""


import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    u_id = sys.argv[1]
    name = requests.get(url + "{}".format(u_id)).json().get('username')
    todos = requests.get(url + "{}/todos".format(u_id)).json()

    filename = f'{u_id}.csv'

    with open(filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow([i['userId'], name, i['completed'], i['title']])
