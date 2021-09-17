import tweepy
from time import sleep
from tokens import * # tokens.py is a file that contains the Twitter API keys

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

url="https://twitter.com/austin_castel/status/"

for status in tweepy.Cursor(api.search, q=('portainer'), lang='en').items(20):
            try:
                a=status.id
                print(url+str(a))
            except Exception:
                print()
 
