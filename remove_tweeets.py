import tweepy
from time import sleep
from tokens import * # tokens.py is a file that contains the Twitter API keys


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

## https://pythonmarketer.com/2020/09/13/delete-all-your-tweets-with-tweepy-and-the-twitter-api/

for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print("Deleted:", status.id)
            except Exception:
                print("Failed to delete:", status.id)
 
        
