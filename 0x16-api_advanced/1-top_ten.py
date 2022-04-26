#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    url = requests.get('https://api.reddit.com/r/{}/hot.json'
                     .format(subreddit),
                     headers={'user-agent': 'kingaris'},
                     allow_redirects=False)
    url_json = url.json()
    if url_json.get('message') == 'Not Found':
        print("None")
        return
    x = url_json.get('data').get('children')
    for i in range(0, 10):
        print(x[i].get('data').get('title'))
