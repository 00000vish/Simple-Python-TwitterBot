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


#UnFavorite
To unfavorite a tweet you would add

```python
unfav(tweet_cid)
```

in ```on_data``` method. 

#Streaming API

```
track_words=["#SriLanka"]
```

This will listen to "#SriLanka" tag live.
 
Lets say if you want to change it to ```"#Hello World"```, you would replace ```"#SriLanka"``` with ```"#Hello World"```

like below.
```python
track_words=["#HelloWorld"]
```

If you want to listen to both you would put both in track like this. 


```python
track_words=["#Hello World", "#SriLanka"]
```

if you want to listen to tweet from a certian account put them in `follow_acc`

```
 follow_acc = ['2312312' , '1234332'] # all username converted to user ids
```



#Ban Account or Words
If you want to not retweet or favorite a tweet from a certian account or tweets with words,
put them into the following arrays.

```python
 accs = ['twitter' , 'twittersupport'] # banned account screen name goes in here
 words = ['hate' , 'derp'] # banned words goes in here
```
