#!/usr/bin/python3
'''use csv format'''
import requests
import sys

if __name__ == '__main__':
    '''Main task with api'''
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_url = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(employee_id)
    t_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(employee_id)
    response = requests.get(t_url)
    todos, employee = response.json(), requests.get(employee_url).json()

    if response.status_code != 200:
        print("Employee with ID {} not found".format(employee_id))
        sys.exit(1)

    csv_f = '{}.csv'.format(employee_id)
    with open(csv_f, 'w') as file:
        for task in todos:
            formatw = '"{}", "{}", "{}", "{}"\n'.format(
                employee_id, employee['username'],
                task['completed'], task['title'])
            file.write(formatw)
