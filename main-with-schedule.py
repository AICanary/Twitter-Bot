import tweepy
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from gnewsclient import gnewsclient
from bs4 import BeautifulSoup
import requests
import pyshorteners
import json

# Twitter API credentials
API_KEY = 'your_twitter_api_key'
API_SECRET_KEY = 'your_twitter_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'


# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_trending_hashtags():
    WOEID = 23424922  # WOEID for Pakistan
    trending_topics = api.get_place_trends(id=WOEID)[0]['trends']
    hashtags = [topic['name'] for topic in trending_topics if topic['name'].startswith('#')]
    english_hashtags = [hashtag for hashtag in hashtags if not any(char.isdigit() for char in hashtag)]
    urdu_hashtags = [hashtag for hashtag in hashtags if any(char.isdigit() for char in hashtag)]
    return english_hashtags[:2] + urdu_hashtags[:1]  # Adjust the number of hashtags to include


def get_latest_google_news():
    news_client = gnewsclient.NewsClient(language='en', location='Pakistan', topic='Headlines', max_results=10)
    news = news_client.get_news()
    return [(item['title'], item['link']) for item in news]

def get_image_url(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    image = soup.find('img')
    return image['src'] if image else None

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

def load_posted_headlines():
    try:
        with open("posted_headlines.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_posted_headlines(headlines):
    with open("posted_headlines.json", "w") as file:
        json.dump(headlines, file)

def post_tweet():
    news_items = get_latest_google_news()
    posted_headlines = load_posted_headlines()

    for headline, link in news_items:
        if headline not in posted_headlines:
            short_link = shorten_url(link)
            hashtags = " ".join(get_trending_hashtags())
            tweet_with_hashtags = f"{headline} {short_link} {hashtags}"
            
            image_url = get_image_url(link)
            if image_url:
                response = requests.get(image_url)
                with open("temp_image.jpg", "wb") as img_file:
                    img_file.write(response.content)
                media = api.media_upload("temp_image.jpg")
                api.update_status(status=tweet_with_hashtags, media_ids=[media.media_id])
                os.remove("temp_image.jpg")
            else:
                api.update_status(status=tweet_with_hashtags)

            print(f"Posted tweet: {tweet_with_hashtags}")
            posted_headlines.append(headline)
            save_posted_headlines(posted_headlines)
            break
    else:
        print("No more headlines to post!")

# Schedule tweets
scheduler = BlockingScheduler()
scheduler.add_job(post_tweet, 'interval', hours=1)  # Posts one tweet every 4 hours
scheduler.start()