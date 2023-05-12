#!/usr/bin/python3
'''Module for reddit api'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''Function for reddit api hot list recurse'''
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    header = {"User-Agent": "user_agent"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=header, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        hposts = data.get('children')
        for post in hposts:
            hot_list.append(post.get('data').get('title'))
        after = data.get('after')
        if after:
            return (recurse(subreddit, hot_list, after=after))
        else:
            return (hot_list)
    else:
        return (None)
