# Simple-Python-TwitterBot 


Simple python code i created for my twitter bots using Tweepy. It is able to listen to keyword and retweet and/or favorite them. Exmaple: [@Jothipala_Bot](https://twitter.com/Jothipala_Bot)


#Video
[![Video](http://i.imgur.com/14lnzbS.png)](http://www.youtube.com/watch?v=OurIac65qqI)


#Requirements 
Tweepy (installed).


Need to have twitter app with Oauth keys and etc.


Python 2.7 or 3.4.


#Oauth
Fill in Oauth info to

* `ckey = 'here'`
* `csecret = 'here'`
* `atoken = 'here'`
* `asecret = 'here'`

#Favorite
To favorite a tweet you would add

```python
 fav(tweet_cid)
```

in ```on_data``` method. 

#Retweet
To retweet a tweet you would add

```python
 retweet(tweet_cid)
```

in ```on_data``` method. 


#UnFavorite
To unfavorite a tweet you would add

```python
 unfav(tweet_cid)
```

in ```on_data``` method. 

#Streaming API

```
 track_words=["#SriLanka"]
 ...
 twt.filter(track= track_words) 
```

This will listen to "#SriLanka" tag live.


If you want to listen to tweets from a certian account:

```
 follow_acc = ['2312312' , '1234332'] # all username converted to user ids
 ...
 twt.filter(follow = follow_acc)
```

If you want to listen to tweets from a certian location:
```
 loc = [-74.255735,40.496044,-73.7002721,40.9152555] #Box cordinations at the location
 ...
 twt.filter(locations=loc)
```


#Bans and Whitelists
If you want to not retweet or favorite a tweet from a certian account or tweets with words,
put them into the following arrays.

```python
 banned_accs = ['twitter' , 'twittersupport'] # banned account screen name goes in here
 banned_words = ['hate' , 'derp'] # banned words goes in here
```

```python
 whitelist_acc = ['twitter' , 'twittersupport'] # banned account screen name goes in here
 whitelist_words = ['Hellow' , 'Daft Punk'] # banned words goes in here
```
