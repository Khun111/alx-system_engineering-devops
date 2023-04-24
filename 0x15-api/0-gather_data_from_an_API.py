#!/usr/bin/python3
"give information about todo progress"
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    t_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(t_url)
    employee = requests.get(employee_url).json()

    if response.status_code != 200:
        print("Employee with ID {} not found".format(employee_id))
        sys.exit(1)
    todos = response.json()

    completed = [todo for todo in todos if todo['completed']]
    employee_name = employee.get('name')
    total_tasks = len(todos)
    len_completed = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len_completed, total_tasks))

    for task in completed:
        print("\t {}".format(task['title']))
