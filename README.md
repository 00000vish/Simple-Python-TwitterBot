# Simple-Python-TwitterBot
simple python code i created for my twitter bot, that will listen to ketword and retweet or favorite it.

Need to have twitter dev account with Oauth keys n etc.

if you dont have one create it here : https://apps.twitter.com/

#Oauth
Fill in Oauth info to

ckey = ''

csecret = ''

atoken = ''

asecret = ''

#favorite
To favorite a tweet you would add

fav(raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", ""))

in on_data method. 

#Stream
This will listen to "#infoleak"

you can change it here -->twt.filter(track=["#infoleak"])


