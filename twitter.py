import os
import requests

# Gets most recent tweets from users in the user list
TWITTER_API = ''

# Username to get tweets from
username = 'cnnbrk'

# Url to the users tweets
url = f'https://api.twitterapi.io/twitter/user/last_tweets?userName=cnnbrk'

headers = {'X-API-Key': TWITTER_API}

# Requests API
response = requests.get(url, headers=headers)
print(response)

tweets = response.json().get("data", {}).get("tweets", [])

for tweet in tweets:
    print(tweet.get("text", "No text"))