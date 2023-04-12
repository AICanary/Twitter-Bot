# Twitter Bot

This is a Twitter bot that posts the latest news headlines from Pakistan along with relevant hashtags.

## Getting Started

### Prerequisites

To run this bot, you'll need:

- Python 3.7 or higher
- tweepy library
- gnewsclient library
- beautifulsoup4 library
- requests library
- pyshorteners library

### Installing

Clone the repository

Install the required libraries using pip:

```pip install tweepy gnewsclient beautifulsoup4 requests pyshorteners```

### Setting up Twitter API Credentials

To use the Twitter API, you'll need to create a developer account and obtain your API credentials. Follow these steps:

1. Go to https://developer.twitter.com/en/apps and sign in with your Twitter account.
2. Click on the "Create an app" button.
3. Fill in the required information and agree to the terms.
4. Once your app is created, go to the "Keys and tokens" tab and copy your API key, API secret key, access token, and access token secret.
5. Open the main.py file and replace the placeholders with your API credentials:

```python
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'


Running the Bot
To run the bot, simply execute the main.py file:

python main.py

The bot will fetch the latest news headlines from Pakistan, add relevant hashtags, and post them on Twitter.

License
This project is licensed under the MIT License - see the LICENSE file for details.
