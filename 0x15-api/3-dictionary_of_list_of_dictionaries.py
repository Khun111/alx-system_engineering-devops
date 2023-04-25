#!/usr/bin/python3
'''use json format'''
import json
import requests
import sys

if __name__ == '__main__':
    '''Main task with api'''
    t_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    response = requests.get(t_url.format(1))
    todos = response.json()
    employees = {}

    for task in todos:
        employee_id = task.get('userId')
        todo = {
            'username': '',
            'task': task.get('title'),
            'completed': task.get('completed')
        }
        if employee_id not in employees:
            employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
            employees[employee_id] = [{'username': employee.get('username'), 'task': task.get('title'), 'completed': task.get('completed')}]
        else:
            employees[employee_id].append({'username': employee.get('username'), 'task': task.get('title'), 'completed': task.get('completed')})

    json_f = 'todo_all_employees.json'
    with open(json_f, 'w') as file:
        json.dump(employees, file)
