#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers for a given subreddit. Returns 0 if an invalid subreddit is given
"""
import requests

def number_of_subscribers(subreddit):
    if (type(subreddit) is not str):
        return(0)
    url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'user-agent': 'kingaris'}
    response = requests.get(url, headers=headers)
    if response.status_code is not 200:
        return(0)
    return(response.json().get("data").get("subscribers"))
