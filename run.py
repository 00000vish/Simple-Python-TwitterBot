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
            tweet_text = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "")
            screen_name = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "")
            tweet_cid = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "")

            accs = ['twitter' , 'twittersupport'] # banned account screen name goes in here
            words = ['hate' , 'derp'] # banned words goes in here

            if not any(acc in screen_name.lower() for acc in accs):
                if not any(word in tweet_text.lower() for word in words):
                    # call what u want to do here
                    #fav(tweet_cid)
                    #retweet(tweet_cid)
            return True
        except Exception as e:
            print(str(e)) # prints the error msg, if u dont want it comment it out
            pass
			

    def on_error(self, status_code):
        try:
            print( "error" + status_code)
        except Exception as e:
            print(str(e))
            pass
			

def retweet(tweet_cid):
    try:
        api.retweet(tweet_cid)
    except Exception as e:
        print(str(e))
        pass


def fav(tweet_cid):
    try:
        api.create_favorite(tweet_cid)
    except Exception as e:
        print(str(e))
        pass


def unfav(tweet_cid):
    try:
        api.destroy_favorite(tweet_cid)
    except Exception as e:
        print(str(e))
        pass


def tweet(myinput):
    try:
        api.update_status(myinput)
    except Exception as e:
        print(str(e))
        pass


try:
    twt = Stream(auths, listener())

    track_words = ["#lka","SriLanka","@Jothipala_Bot","@SiripalaBot"]
    follow_acc = ['2312312' , '1234332'] # all username converted to user ids
    twt.filter(track= track_words , follow = follow_acc)
except Exception as e:
    print(str(e))
    pass