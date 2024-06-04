#!/usr/bin/python3
"""
Query Reddit API for frist 10 subreddit posts.
"""
import requests


def top_ten(subreddit):
    """Print the titles for top posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))
    else:
        print("None")
        return
