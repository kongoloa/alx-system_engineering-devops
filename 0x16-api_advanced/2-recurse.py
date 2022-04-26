#!/usr/bin/python3
"""
 A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    if after is not None:
        url = 'https://api.reddit.com/r/' +\
              '{}/hot.json?after={}'.format(subreddit, after)
    else:
        url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'user-agent': 'ianscustomthing'}

    r = requests.get(url,
                     headers=header,
                     allow_redirects=False)
    rj = r.json()
    if rj.get('message') == 'Not Found':
        return
    chldrn = rj.get('data').get('children')
    hot_list += [chld.get('data').get('title') for chld in chldrn]
    after = rj.get('data').get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
