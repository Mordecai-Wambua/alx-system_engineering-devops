#!/usr/bin/python3
"""
Find titles for hot articles using Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return list of article titles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get("after")
        for post in data.get("children"):
            hot_list.append(post.get('data').get('title'))
    else:
        return None

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
