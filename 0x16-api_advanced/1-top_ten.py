  
#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed"""
import requests
from sys import argv


def top_ten(subreddit):
    url_redd = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url_redd += "?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url_redd, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        print(None)
        return
    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")
    top_10_posts = ""
    for post in hot_posts_json:
        top_10_posts += post.get("data").get("title") + "\n"
    print(top_10_posts, end="")