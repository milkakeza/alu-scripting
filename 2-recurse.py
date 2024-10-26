#!/usr/bin/python3
""" a recursive function that queries the Reddit API 
and returns a list containing the titles of all hot articles for a given subreddit. """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ the function returns list with titles of all hot articles in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Reddit-hot-articles-titles-checker/1.0'}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        if data["after"] is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data["after"])
    elif response.status_code == 404:
        return None