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

#whitelist handles and words
whitelist_acc = []

#banned handles and words
banned_accs =  []
banned_words = []

track_words = [] #retweet any tweet with these words
follow_accs = [] #retweet every tweet from this accounts, handles converted to ids
location = [-74.255735,40.496044,-73.7002721,40.9152555] #reteet any tweet with goelocation that matches this box


class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            tweetText = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "")  # tweet's text
            userName = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "")  # tweet's authors screen name
            tweetId = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "")  # tweet's id

            if (userWhitelist(userName) or (userBanned(userName) and safeForWork(tweetText))):
                like(tweetId)
            print("https://twitter.com/" + userName  + "/status/"  + tweetId)
            print("WHITELIST: " + str(userWhitelist(userName)) + "  BANNED: " + str(not userBanned(userName)) + "  TEXTSAFE: " + str(safeForWork(tweetText)))
            print("")
            return True
        except Exception as e:
            print(str(e))  # prints the error msg, if u dont want it comment it out
            restart()
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

def like(tweetId):
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

def getBanWords():
    with open("BannedWords.txt") as ins:
        for line in ins:
            if "#DO_NOT_REMOVE_THIS_LINE#" not in str(line):
                banned_words.append(line.strip())

def getBanAccounts():
    with open("BannedAccounts.txt") as ins:
        for line in ins:
            if "#DO_NOT_REMOVE_THIS_LINE#" not in str(line):
                banned_accs.append(line.strip())

def getTrackWords():
    with open("TrackWords.txt") as ins:
        for line in ins:
            if "#DO_NOT_REMOVE_THIS_LINE#" not in str(line):
                track_words.append(line.strip())

def getFollowAccounts():
    with open("FollowAccounts.txt") as ins:
        for line in ins:
            if "#DO_NOT_REMOVE_THIS_LINE#" not in str(line):
                follow_accs.append(line.strip())

def restart():
    print("Restart....")
    startBot()

def startBot():
    print("")
    print("Initializing....")
    getBanAccounts()
    print("getting banned accounts....check")
    getBanWords()
    print("getting banned words....check")
    getTrackWords()
    print("getting track words....check")
    getFollowAccounts()
    print("getting follow accounts....check")
    print("")
    print("""\

 _____       _ _   _           _____ _____ _____
|_   _|_ _ _|_| |_| |_ ___ ___| __  |     |_   _|
  | | | | | | |  _|  _| -_|  _| __ -|  |  | | |
  |_| |_____|_|_| |_| |___|_| |_____|_____| |_|
             created by vishwenga

Running.... :)                    """)
    try:
        twt = Stream(auths, listener())
        twt.filter(track=track_words)
    except Exception as e:
        print(str(e))
        pass

startBot()
