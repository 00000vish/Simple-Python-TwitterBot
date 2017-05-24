# Simple-Python-TwitterBot 


Simple python code i created for my twitter bots using Tweepy. It is able to listen to keyword and retweet and/or favorite them. Exmaple: [@Jothipala_Bot](https://twitter.com/Jothipala_Bot)


# Video
[![Video](http://i.imgur.com/14lnzbS.png)](http://www.youtube.com/watch?v=OurIac65qqI)


# Requirements 
Tweepy (installed).


Need to have twitter app with Oauth keys and etc.


Python 3.4 recommended.


# Oauth
Fill in Oauth info to

* `ckey = 'here'`
* `csecret = 'here'`
* `atoken = 'here'`
* `asecret = 'here'`

# Like
To like a tweet you would add

```python
 like(tweet_cid)
```

in ```on_data``` method. 

# Retweet
To retweet a tweet you would add

```python
 retweet(tweet_cid)
```

in ```on_data``` method. 


# UnLike
To unlike a tweet you would add

```python
 unlike(tweet_cid)
```

in ```on_data``` method. 

# Streaming API

If you want to listen to cretain words:

``` 
 twt.filter(track= track_words) 
```
Provide the track words list in TrackWords.txt file.


If you want to listen to tweets from a certian account:

```
 twt.filter(follow = follow_acc)
```
Provide the follow accounts in FollowAccounts.txt file.


If you want to listen to tweets from a certian location:
```
 loc = [-74.255735,40.496044,-73.7002721,40.9152555] #Box cordinations at the location
 ...
 twt.filter(locations=loc)
```


# Bans and Whitelists
If you want to not retweet or favorite a tweet from a certian account or tweets with words,
put them into thier corresponding textfiles. For exmaple if you want to ban a word, add it to 
the BannedWords.txt or if you want to ban an account add the username to the BannedAccounts.txt file.
Also if you want to whitelist an account add its username to WhitelistAccounts.txt file.
