# Simple-Python-TwitterBot ```in progress, more features to come```
Simple python code i created for my twitter bot. It is able to listen to ketword and retweet and/or favorite it.


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
fav(raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", ""))
```

in ```on_data``` method. 


#UnFavorite
To favorite a tweet you would add

```python
unfav(raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", ""))
```

in ```on_data``` method. 

#Streaming API
This will listen to "#SriLanka" tag live.
 
Lets say if you want to change it to ```"#Hello World"```, you would replace ```"#SriLanka"``` with ```"#Hello World"```

like below.
```python
twt.filter(track=["#Hello World"])
```

If you want to listen to both you would put both in track like this.

```python
twt.filter(track=["#Hello World", "#SriLanka"])
```


