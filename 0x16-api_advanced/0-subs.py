#!/usr/bin/python3
"""returns the number of subscribers"""
import requests
from sys import argv

def number_of_subscribers(subreddit):
    url_redd = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url_redd, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return 0
    r_json = response.json()
    num_subs = r_json.get("data").get("subscribers")
    return num_subs