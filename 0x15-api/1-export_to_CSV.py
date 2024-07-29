#!/usr/bin/python3
"""gather data from an API and save at csv file"""
import csv
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]

        users_response = requests.get(f'{url}users/{employee_id}')

        user_data = users_response.json()
        employee_name = user_data['name']

        params = {
            'userId': employee_id
        }
        todos_response = requests.get(f'{url}/todos', params=params)
        todos_data = todos_response.json()

        with open(f'{employee_id}.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos_data:
                csv_writer.writerow([str(employee_id), str(employee_name),
                                    str(todo['completed']), str(todo['title'])]
                                    )
