#!/usr/bin/python3
import requests
import sys


employee_id = sys.argv[1]

url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

users_response = requests.get(url)

user_data = users_response.json()  # dict
employee_name = user_data['name']


url = 'https://jsonplaceholder.typicode.com/todos'

params = {
    'userId': employee_id
}
todos_response = requests.get(url, params=params)
todos_data = todos_response.json()

done_tasks = 0
total_tasks = len(todos_data)
completed_tasks = []
for todo in todos_data:
    if todo['completed']:
        done_tasks += 1
        completed_tasks.append(todo['title'])

print(
    f"Employee {employee_name} is done with tasks "
    f"({done_tasks}/{total_tasks}):"
)


for i in completed_tasks:
    print(f"\t {i}")
