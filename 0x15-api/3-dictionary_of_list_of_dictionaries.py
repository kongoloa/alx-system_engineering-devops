#!/usr/bin/python3
""" accessing a url with employee ID to return information """
from json import dump
from requests import get

USERS = 'https://jsonplaceholder.typicode.com/users'
TODOS = 'https://jsonplaceholder.typicode.com/todos'

if __name__ == '__main__':
    with open('todo_all_employees.json', 'w') as ostream:
        dump({
            str(user['id']): [{
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed'],
            } for task in get(TODOS, params={'userId': user['id']}).json()]
            for user in get(USERS).json()
        }, ostream)
