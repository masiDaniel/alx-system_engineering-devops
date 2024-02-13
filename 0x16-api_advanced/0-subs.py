#!/usr/bin/python3
""" query Reddit API, return number of subs for a
 subreddit. """

import requests


def number_of_subscribers(subreddit):
    """ the function """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers).json()

    if response.get("error") == 404:
        return 0
    return response.get("data").get("subscribers")