from distutils.command.sdist import sdist
import os
import tweepy
from loguru import logger
import feedparser






# Create a function to get date from URL
# Create a function to pass a link and then it would return if the blog in the link is newer than the blog posted on the last date
# If true is returned than post and then function for the latest tweet will be called. As latest tweet is called: Newest date will be fetched fromt the link. Then, repeat
# Can work with x links stored in the file

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


USERNAME = 'hrittikhere'
tweets_list = api.user_timeline(USERNAME, count=1)

tweet = tweets_list[0]  # An object of class Status (tweepy.models.Status)
print(tweet.created_at)  # Print the datetime object for the tweet
print(tweet.text)  # Print the text of the tweet
print(tweet.in_reply_to_screen_name)


# https://gist.github.com/JoseIVP/f9b964eb9442cd0e0955249ea6395014


print(dir(tweet))
