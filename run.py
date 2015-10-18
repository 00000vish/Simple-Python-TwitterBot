#!/usr/local/bin/python3.3
import tweepy

from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener, Stream

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auths = OAuthHandler(ckey, csecret)
auths.set_access_token(atoken, asecret)
api = tweepy.API(auths)


class listener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", ""))
        # .split('"id":')[1].split('"id_str":')[0].replace(",", "")
        retweet(raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", ""))
        return True

    def on_error(self, status_code):
        print( "error" + status_code)


# twt = Stream(auths, listener())
#   twt.filter(track=["sl"])


def retweet(myid):
    api.retweet(myid)
    print( "retweeted")


def fav(myid):
    api.create_favorite(myid)


def unfav(myid):
    api.destroy_favorite(myid)


def tweet(myinput):
    api.update_status(myinput)


twt = Stream(auths, listener())
twt.filter(track=["#infoleak"])
# fav(input())
