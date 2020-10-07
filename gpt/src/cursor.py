import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key= 'hi' # Don't have these in the final
consumer_secret= 'hi'# Don't have these in the final
access_token= 'hi'# Don't have these in the final
access_token_secret= 'hi'

authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
authorization.set_access_token(access_token, access_token_secret)

twitter = tweepy.API(authorization, wait_on_rate_limit=True)

def input():
    search_words = "boston celtics -filter:retweets"
    tweets = tweepy.Cursor(twitter.search,
                           q = search_words,
                           lang='en').items(1)
    # for tweet in tweets:
    for tweet in tweets:
        return tweet.text, tweet.id, tweet.user.screen_name

    # return print([tweet.text for tweet in tweets])

input()
