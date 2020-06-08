import os
import tweepy as tw
import pandas as pd
import api_keys 
consumer_key = api_keys.consumer_key
consumer_secret = api_keys.consumer_secret
access_token = api_keys.access_token
access_token_secret= api_keys.access_token_secret

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#animationpaidme"
new_search = search_words + " -filter:retweets"
date_since = "2020-05-30"

tweets = tw.Cursor(api.search, 
                   q=new_search,
                   lang="en", 
                   since=date_since,
                   tweet_mode="extended").items(1200)
info = [[tweet.user.screen_name, tweet.user.location, tweet.full_text ] for tweet in tweets]
tweet_data = pd.DataFrame(data = info,
              columns=[
                  "user", 
                  "location" , 
                  "text"
                       ])
with open("animation_pay.csv", mode='w') as file:
    file.write(tweet_data.to_csv(encoding='utf-8'))