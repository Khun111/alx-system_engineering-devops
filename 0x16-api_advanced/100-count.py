#!/usr/bin/python3
'''Module for reddit api'''

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    '''Function for count_words recurse case-insensitive'''
    if not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "user_agent"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    hposts = data.get("children")
    for post in hposts:
        title = post.get("data").get("title")
        for word in word_list:
            lower_title = title.lower()
            lower_word = word.lower()
            if lower_word not in counts:
                counts[lower_word] = 0
            counts[lower_word] += lower_title.count(lower_word)

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after=after, counts=counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
