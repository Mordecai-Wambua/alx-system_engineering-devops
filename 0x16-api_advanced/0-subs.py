#!/usr/bin/python3
"""Reddit API: Finding subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return number if subscribers for given subreddit."""
    url = "https://www.reddit.com/r/"
    headers = {'User-Agent': 'my_app/0.0.1 (by /u/Crazy_Bowler_5441)'}
    response = requests.get(url+f'{subreddit}/about.json', headers=headers)

    if response.status_code == 200:
        dic = response.json()
        output = dic['data']['subscribers']
        return(output)
    else:
        return(0)
