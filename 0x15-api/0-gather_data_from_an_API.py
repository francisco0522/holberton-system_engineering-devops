#!/usr/bin/python3
"""returns information about his/her TODO list progress."
"""
import requests
from sys import argv

if __name__ == "__main__":
    num_id = argv[1]
    id_info = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(num_id)).json()
    all_task = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(num_id)).json()
    name_employee = id_info.get("name")
    total_num_task = 0
    done_task = 0
    for tasks in all_task:
        total_num_task = total_num_task + 1
        if tasks.get("completed"):
            done_task = done_task + 1
    output = "Employee {} is done with tasks({}/{}):".format(
                name_employee, done_task, total_num_task)
    for tasks in all_task:
        if tasks.get("completed"):
            title = tasks.get("title")
            output += "\n\t " + title
    print(output)
