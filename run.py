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
        try:
            retweet(raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", ""))
            return True
        except Exception:
            pass
			

    def on_error(self, status_code):
        try:
            print( "error" + status_code)
        except Exception:
            pass
			

def retweet(myid):
    try:
        api.retweet(myid)
    except Exception:
        pass


def fav(myid):
    try:
        api.create_favorite(myid)
    except Exception:
        pass


def unfav(myid):
    try:
        api.destroy_favorite(myid)
    except Exception:
        pass


def tweet(myinput):
    try:
        api.update_status(myinput)
    except Exception:
        pass


try:
    twt = Stream(auths, listener())
    twt.filter(track=["#lka","SriLanka","@Jothipala_Bot","@SiripalaBot"])
except Exception:
    pass