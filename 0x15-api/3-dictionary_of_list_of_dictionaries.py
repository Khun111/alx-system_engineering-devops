#!/usr/bin/python3

'''use json format'''
import json
import requests
import sys

if __name__ == '__main__':
    '''Main task with api'''
    t_url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(t_url)
    todos = response.json()
    employees = {}

    for task in todos:
        employee_id = task.get('userId')
        if employee_id not in employees:
            employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
            employees[employee_id] = {'username': employee.get('username'), 'tasks': []}
        todo = {
            'task': task.get('title'),
            'completed': task.get('completed')
        }
        employees[employee_id]['tasks'].append(todo)

    json_f = 'todo_all_employees.json'
    with open(json_f, 'w') as file:
        json.dump(employees, file)
