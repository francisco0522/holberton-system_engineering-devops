#!/usr/bin/python3
"""export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    employ = "https://jsonplaceholder.typicode.com/users"
    employs = requests.get(employ).json()
    report = {}
    for employ in employs:
        id_employee = employ.get("id")
        url_todos = employs + "/{}/todos".format(id_employee)
        r_todos = requests.get(url_todos).json()
        username = employ.get("username")
        total_num_task = r_todos
        list_dict_report = []
        for task in total_num_task:
            id_report = {}
            id_report["username"] = str(username)
            id_report["completed"] = task.get("completed")
            id_report["task"] = str(task.get("title"))
            list_dict_report.append(id_report)
        report[id_employee] = list_dict_report
    with open("todo_all_employees.json", "w") as fjson:
        fjson.write(json.dumps(report))
