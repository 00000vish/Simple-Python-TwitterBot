# Simple-Python-TwitterBot 
#```in progress, more features to come```
Simple python code i created for my twitter bot. It is able to listen to ketword and retweet and/or favorite it.

Exmaples:  
@Jothipala_Bot  :  https://twitter.com/Jothipala_Bot  

@WinnipegWatch  :  https://twitter.com/WinnipegWatch
           

Need to have twitter app with Oauth keys and etc.

if you dont have one create it here : https://apps.twitter.com/

#Oauth
Fill in Oauth info to

* `ckey = ''
* `csecret = ''
* `atoken = ''
* `asecret = ''

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
