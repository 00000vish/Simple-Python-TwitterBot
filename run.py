#!/usr/local/bin/python2.7
import tweepy
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener, Stream

ckey = ''
csecret = ''
atoken = '-'
asecret = ''

auths = OAuthHandler(ckey, csecret)
auths.set_access_token(atoken, asecret)
api = tweepy.API(auths)

#whitelist handles and words goes in here
whitelist_acc = ['','']

#banned handles and words goes in here
banned_accs =  ['','']
banned_words = ['', '']

class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            isRetweeted = raw_data.lower().split('"retweeted":')[1].split(',"possibly_sensitive"')[0].replace(",", "")
            tweetText = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "")  # tweet's text
            userName = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "")  # tweet's authors screen name
            tweetId = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "")  # tweet's id

            if (userWhitelist(userName) or (userBanned(userName) and safeForWork(tweetText))):
                retweet(tweetId)           
            print("https://twitter.com/" + userName  + "/status/"  + tweetId)
            print("WHITELIST: " + str(userWhitelist(userName)) + "  BANNED: " + str(not userBanned(userName)) + "  TEXTSAFE: " + str(safeForWork(tweetText)))
            return True    
        except Exception as e:
            print(str(e))  # prints the error msg, if u dont want it comment it out
            pass

    def on_error(self, status_code):
        print("error " + status_code)

def userWhitelist(userName):
    if any(a_acc == userName.lower() for a_acc in whitelist_acc):
        return True
    return False

def userBanned(userName):
    if not any(acc == userName.lower() for acc in banned_accs):
        return True
    return False

def safeForWork(tweetText):
    if not any(word in tweetText.lower() for word in banned_words):
        return True
    return False

def retweet(tweetId):
    try:
        api.retweet(tweetId)
    except Exception as e:
        print(str(e))
        pass

def fav(tweetId):
    try:
        api.create_favorite(tweetId)
    except Exception as e:
        print(str(e))
        pass

def tweetPost(tweetText):
    try:
        api.update_status(status=tweetText)
    except Exception as e:
        print(str(e))
        pass

track_words = ["Sri Lanka"] #retweet any tweet with these words
follow_acc = ['20536157',"20573247"] #retweet every tweet from this accounts, handles converted to ids
loc = [-74.255735,40.496044,-73.7002721,40.9152555] #reteet any tweet with goelocation that matches this box

print("Running...")
try:
    twt = Stream(auths, listener())
    twt.filter(track=track_words)
except Exception as e:
    print(str(e))
    pass
