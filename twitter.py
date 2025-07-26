import requests
import time
from datetime import datetime, timedelta, timezone

# Configuration
API_KEY = "c00f411d83684781ae233b7483a4695c"
TARGET_ACCOUNT = "BBCNews"  # The account to monitor
CHECK_INTERVAL = 300 # Time between each check
LAST_CHECKED_TIME = datetime.now(timezone.utc) - timedelta(hours=1) # Sets last checked time to 1hr ago

def new_tweets():
    global LAST_CHECKED_TIME
    
    # Format times for the API query
    until_time = datetime.now(timezone.utc)
    since_time = LAST_CHECKED_TIME
    
    # Format times as strings in the format API expects
    since_str = since_time.strftime("%Y-%m-%d_%H:%M:%S_UTC")
    until_str = until_time.strftime("%Y-%m-%d_%H:%M:%S_UTC")
    
    # Construct the query
    query = f"from:{TARGET_ACCOUNT} since:{since_str} until:{until_str} include:nativeretweets"
    
    # API endpoint
    url = "https://api.twitterapi.io/twitter/tweet/advanced_search"
    
    # Request parameters
    params = {
        "query": query,
        "queryType": "Latest"
    }
    
    # Headers with API key
    headers = {
        "X-API-Key": API_KEY
    }
    
    all_tweets = []

    response = requests.get(url, headers=headers, params=params)
    
    # Parse the response
    if response.status_code == 200:
        data = response.json()
        tweets = data.get("tweets", [])
        
        if tweets:
            all_tweets.extend(tweets)
            

    # Process all collected tweets
    if all_tweets:
        print(f"Found {len(all_tweets)} total tweets from {TARGET_ACCOUNT}!")
        for tweet in all_tweets:
            print(f"{tweet['text']}")
            # TODO Analyse tweets
    else:
        print(f"No new tweets from {TARGET_ACCOUNT} since last check.")
    
    # Update the last checked time
    LAST_CHECKED_TIME = until_time

# Main monitoring loop
def main():
    print(f"Starting to monitor tweets from @{TARGET_ACCOUNT}")
    print(f"Checking every {CHECK_INTERVAL} seconds")
    
    try:
        while True:
            new_tweets()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

main()