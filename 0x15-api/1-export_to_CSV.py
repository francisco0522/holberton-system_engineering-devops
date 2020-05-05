#!/usr/bin/python3
"""
    Uses the fake API to get an employer and export the info in csv formater
"""
import csv
import requests
from sys import argv

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
    name_employee = id_info.get("username")
    list_report = []
    for task in all_task:
        report = {}
        report["USER_ID"] = str(task.get("userId"))
        report["USERNAME"] = str(name_employee)
        report["TASK_COMPLETED_STATUS"] = str(task.get("completed"))
        report["TASK_TITLE"] = str(task.get("title"))
        list_report.append(report)
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open("{}.csv".format(num_id), "w") as fcsv:
        f_csv = csv.DictWriter(fcsv, fieldnames=header, quoting=csv.QUOTE_ALL)
        f_csv.writerows(list_report)