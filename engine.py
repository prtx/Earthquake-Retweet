#/usr/bin/python3
# -*- coding: utf-8 -*-

import tweepy
import json
import sys
import time
import keys


include = [
    'ambulance',
    'volunteer',
    'need',
    'relief',
    'contact',
    'emergency',
    'food',
    'water',
    'blood',
    'tent',
    'hospital'
]

exclude = [
    'donate',
    '~rt ',
    'gospel',
    'pray',
    '?'
]

places = open('places.txt').read().split()


def list_on_tweet(array, tweet):
    
    for word in array:
        if word in tweet:
            return True
    

class StdOutListener(tweepy.StreamListener):
    
    i = 0
    check_time = time.time()
    posted_tweets = []
    
    def on_data(self, data):
    
        csv = open('tweets.csv', 'a')
        self.i += 1
        tweet = json.loads(data)
        print(tweet['text'])
        csv.write(
            str(self.i)+'\t'+                                                   #S.no
            str(tweet['id'])+'\t'+                                              #tweet id
            tweet['user']['id_str']+'\t'+                                       #user id
            tweet['user']['name'].replace('\t',' ').replace('\n',' ')+'\t'+     #name
            tweet['user']['location'].replace('\t',' ').replace('\n',' ')+'\t'+ #location
            tweet['text'].replace('\t',' ').replace('\n',' ')+'\t'+             #tweet
            tweet['created_at']+'\t'+                                           #datetime
            str(tweet['favorite_count'])+'\t'+                                  #favorite count
            str(tweet['retweet_count'])+'\n'                                    #RT count
        )
        
        tweet_to_include = list_on_tweet(include, tweet['text'].lower())
        tweet_to_exclude = list_on_tweet(exclude, '~'+tweet['text'].lower())
        new_tweet = tweet['text'] not in self.posted_tweets

        if tweet_to_include and not tweet_to_exclude and new_tweet:
            _api.retweet(id=tweet['id'])
            try:
                self.posted_tweets.append(tweet['text'])
                print('retweeted')
            except Exception:
                pass
            
        
        if self.i%18000 == 0:
            while True:
                print(time.time() - check_time)
                if time.time() - check_time > 900:
                    break
        return True


    def on_error(self, status):
        print(status)


def tracker():

    key1 = keys.key1
    key2 = keys.key2
    
    tweetslist = []
    l = StdOutListener()
    auth = tweepy.OAuthHandler(key1.consumer_key, key1.consumer_secret)
    auth.set_access_token(key1.access_token, key1.access_token_secret)
    api = tweepy.API(auth)
    
    _auth = tweepy.OAuthHandler(key2.consumer_key, key2.consumer_secret)
    _auth.set_access_token(key2.access_token, key2.access_token_secret)
    _api = tweepy.API(_auth)

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#nepalquakerelief', '#earthquakenepal', 'earthquake'], async = True)


if __name__ == '__main__':    
    tracker()
