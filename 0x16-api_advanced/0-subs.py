#!/usr/bin/python3
import requests
def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "user_agent"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return (data.get('data').get('subscribers'))
    else:
        return (0)
