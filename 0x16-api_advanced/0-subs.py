#!/usr/bin/python3
'''Module for reddit api'''
import requests


def number_of_subscribers(subreddit):
    '''Function for reddit api subscribers'''
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
