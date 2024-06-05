#!/usr/bin/python3
"""
Reddit API usage for finding subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """Return number if subscribers for given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        dic = response.json().get('data')
        return dic.get('subscribers')
    else:
        return 0
