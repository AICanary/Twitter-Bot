import requests
from requests.structures import CaseInsensitiveDict
import json
from datetime import datetime

# Your Twitter Developer API credentials
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFfvSQAAAAAAmEdnoFj98L48Kk9%2BfhwCtuwAZBQ%3D19hRVgfEioD3AlgUBfmNv9IJqerVOjpXqPBXiwzRtI48L9ETQa'

# Function to create the authorization header for requests
def create_headers(bearer_token):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {bearer_token}"
    headers["Content-Type"] = "application/json"
    return headers

# Function to post a tweet
def post_tweet(bearer_token, tweet_text):
    url = 'https://api.twitter.com/2/tweets'

    headers = create_headers(bearer_token)

    data = {
        "status": tweet_text
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 201:
        raise Exception(f"Error posting tweet: {response.status_code} - {response.text}")

    print("Tweet posted successfully!")

# Main function to get the date and post the tweet
def main():
    # Get today's date
    today = datetime.today().strftime('%Y-%m-%d')

    # Prepare the tweet text
    tweet_text = f"Today's Date is {today}"

    # Post the tweet
    post_tweet(BEARER_TOKEN, tweet_text)

if __name__ == "__main__":
    main()
