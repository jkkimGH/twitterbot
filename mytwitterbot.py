import sys
import time, random
import simple_twit
from tweet import get_tweet_components as gtc

CONSUMER_KEY = "" # <-- Your Twitter Dev API key goes here
CONSUMER_SECRET = "" # Your Twitter Dev API key secret goes here

def twitterbot(api):
    simple_twit.send_media_tweet(api, str(gtc()[0]), gtc()[1])

if __name__ == "__main__":
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)
    twitterbot(api)
