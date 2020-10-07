import tweepy
import datetime
import time
# import pandas as pd
# import numpy as np
# from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key= 'hi' # Don't have these in the final
consumer_secret= 'hi'# Don't have these in the final
access_token= 'hi'# Don't have these in the final
access_token_secret= 'hi'# Don't have these in the final

# Using the keys, setup the authorization
authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
authorization.set_access_token(access_token, access_token_secret)

twitter = tweepy.API(authorization)


def update_status(text, id):
    status = twitter.update_status(text,
    # in_reply_to_status_id=id
    )
    return status
