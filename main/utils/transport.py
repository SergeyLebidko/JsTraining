import requests


URL = 'https://jsonplaceholder.typicode.com/users'


def send_request():
    req = requests.get(URL)
    return req.json()
