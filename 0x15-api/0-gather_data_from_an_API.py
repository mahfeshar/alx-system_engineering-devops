#!/usr/bin/python3
"""gather data from an API and display completed tasks"""
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])

        users_response = requests.get(f'{url}users/{employee_id}')

        user_data = users_response.json()
        employee_name = user_data['name']

        params = {
            'userId': employee_id
        }
        todos_response = requests.get(f'{url}/todos', params=params)
        todos_data = todos_response.json()

        completed_tasks = []
        for todo in todos_data:
            if todo['completed']:
                completed_tasks.append(todo['title'])

        print(
            f"Employee {employee_name} is done with tasks "
            f"({len(completed_tasks)}/{len(todos_data)}):"
        )

        for i in completed_tasks:
            print(f"\t {i}")
