# Import the libraries
import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler
# credentials
consumer_key = "@trucdeptrai"
consumer_secret = "truc102160170"
access_token = "tieuthu.anninh@gmail.com"
access_token_secret = "truc102160170"
# calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Provide the query you want to pull the data. For example, pulling data for the mobile phone ABC
query ="ABC"
# Fetching tweets
Tweets = api.search(query, count = 10,lang='en',exclude='retweets',tweet_mode='extended')