#!/usr/bin/env python
# coding: utf-8

import json
import csv
import tweepy
import re

def find_hashtags(api_key, api_secret_key, access_token, access_token_secret, hashtag_phrase):
    
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    try:
        fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))
    except:
        fname = re.findall(r"#(\w+)", hashtag_phrase)

    with open('%s.csv' % (fname), 'w') as file:

        w = csv.writer(file)
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(100):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])


consumer_key = input('API Key - ')
consumer_secret = input('API Secret - ')
access_token = input('Access Token - ')
access_token_secret = input('Access Token Secret - ')
    
hashtag_phrase = input('Hashtag Phrase - ')

if __name__ == '__main__':
    find_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)