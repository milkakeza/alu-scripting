#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """
    number count of subscribers
    """
    url= "https://reddit.com/r/{programmerHumor}/about.json"
    headers = {"User-Agent": "reddit-subscriber-checker/1.0 (by u/Beautiful_Bird9169)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
