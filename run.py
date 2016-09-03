#!/usr/local/bin/python2.7
import tweepy
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler

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
            retweet_ed = raw_data.lower().split('"retweeted":')[1].split(',"possibly_sensitive"')[0].replace(",", "")
            tweet_text = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "") #tweet's text
            screen_name = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "") #tweet's authors screen name
            tweet_sid = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "") #tweet's id

			#whitelist handles and words goes in here
            whitelist_acc = [' ', ' ']
            whitelist_words = [' ', ' ']

            #banned handles and words goes in here
            banned_accs =  [' ' ,' ']
            banned_words = [' ' ,' ']

            if not any(a_acc == screen_name.lower() for a_acc in whitelist_acc):
                if not any(acc == screen_name.lower() for acc in banned_accs):
                    if not any(a_wrds in screen_name.lower() for a_wrds in whitelist_words):
                        if not any(word in tweet_text.lower() for word in banned_words):
                            if("false" in retweet_ed):
                                #call what u want to do here
                                #for example :
                                #fav(tweet_sid)
                                #retweet(tweet_sid)
                            else:
                                #call what u want to do here
                                #for example :
                                #fav(tweet_sid)
                                #retweet(tweet_sid)
            return True
        except Exception as e:
            print(str(e)) # prints the error msg, if u dont want it comment it out
            pass

    def on_error(self, status_code):
        try:
            print( "error " + status_code)
        except Exception as e:
            print(str(e))
        pass


def retweet(tweet_sid):
    try:
        api.retweet(tweet_sid)
    except Exception as e:
        print(str(e))
        pass


def fav(tweet_sid):
    try:
        api.create_favorite(tweet_sid)
    except Exception as e:
        print(str(e))
        pass

def tweetPost(tweet_text):
    try:
        api.update_status(status=tweet_text)
    except Exception as e:
        print(str(e))
        pass

track_words = [" "," "," "] #retweet any tweet with these words
follow_acc = ['20536157',"20573247"] #retweet every tweet from this accounts, handles converted to ids
loc = [-74.255735,40.496044,-73.7002721,40.9152555] #reteet any tweet with goelocation that matches this box

print("Running...")
try:
    twt = Stream(auths, listener())
    twt.filter(track= track_words) # OR (follow = follow_acc)  OR  (locations=loc)
except Exception as e:
    print(str(e))
    pass
