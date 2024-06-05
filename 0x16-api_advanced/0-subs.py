#!/usr/bin/python3
"""Reddit API usage for finding subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return number if subscribers for given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent":
            "Linux:0x16.api.advanced:v1.0.0 (by /u/Crazy_Bowler_5441"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")
