#!/usr/bin/python3
""" export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    num_id = argv[1]
    id_info = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(num_id)).json()
    all_task = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(num_id)).json()
    name_employee = id_info.get("username")
    list_dict_report = []
    for task in all_task:
        id_report = {}
        id_report["username"] = str(name_employee)
        id_report["completed"] = task.get("completed")
        id_report["task"] = str(task.get("title"))
        list_dict_report.append(id_report)
    report = {}
    report[num_id] = list_dict_report
    with open("{}.json".format(num_id), "w") as fjson:
        fjson.write(json.dumps(report))
