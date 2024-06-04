#!/usr/bin/python3
"""Reddit API: Finding subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return number if subscribers for given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_app/0.0.1 (by /u/Crazy_Bowler_5441)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        dic = response.json()
        output = dic['data']['subscribers']
        return(output)
    else:
        return(0)
