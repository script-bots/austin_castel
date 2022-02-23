import os #for secrets
import tweepy
from time import sleep
from loguru import logger


CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True) # https://stackoverflow.com/questions/41786569/twitter-error-code-429-with-tweepy
#https://stackoverflow.com/questions/58844898/how-to-follow-someone-on-twitter-using-tweepy-python

# #kubernetes OR #cncf OR #prometheus OR #portainer OR #gitlab OR #k3s OR #python OR #golang 

for tweet in tweepy.Cursor(api.search, q=('kubernetes OR #cncf OR #gitlab OR #k3s OR #portainer'), lang='en').items(10):
    try:
        
        identity=tweet.id
        status = api.get_status(identity)
        logger.debug((status.text))
        tagss=status.entities["hashtags"]
        logger.warning((tagss))
        for tags in tagss:
            logger.info((tags["text"]))


        # print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        # tweet.retweet()
        # print('Retweeted the tweet')

        # sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
