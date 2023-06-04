import os
import tweepy
from time import sleep
from loguru import logger



CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# https://stackoverflow.com/questions/41786569/twitter-error-code-429-with-tweepy
api = tweepy.API(auth, wait_on_rate_limit=True)
# https://stackoverflow.com/questions/58844898/how-to-follow-someone-on-twitter-using-tweepy-python

# #kubernetes OR #cncf OR #prometheus OR #portainer OR #gitlab OR #k3s OR #python OR #golang

for tweet in tweepy.Cursor(api.search, q=('kubernetes OR #cncf OR #gitlab OR #k3s'), lang='en').items(400):
    try:
        identity = tweet.id
        status = api.get_status(identity, tweet_mode = "extended")
        logger.debug((status.full_text))
#         logger.debug(status.id)
        tagss = status.entities["hashtags"]
#         logger.warning(type(tagss))
        counter = len(tagss)
        logger.debug(counter)
        for tags in tagss:
            logger.debug((tags["text"]))
#         name = status.user.screen_name
#         temp_name = 'hrittikhere'
        link="https://twitter.com/hrittikhere/status/"+str(identity)
        # if counter<=3 and name==temp_name:

        if counter <= 3:

            tweet.retweet()
            logger.critical(link)
            logger.debug("POSTED 🔝")
        else:
            logger.critical(link)
            logger.critical("Not Posted  🔝")

        # print('\nTweet by: @' + tweet.user.screen_name)
        # sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
