#!/usr/bin/python3
'''Module for reddit api'''
import requests


def top_ten(subreddit):
    '''Function for reddit api hot posts'''
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "user_agent"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data').get('title'))
    else:
        print(None)
