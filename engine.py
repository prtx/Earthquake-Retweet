import tweepy,json,sys,time
from keys import all_keys

# -*- coding: utf-8 -*-
reload(sys)
sys.setdefaultencoding('utf8')

include = ['ambulance','volunteer','need','relief','contact','emergency','food','water','blood','tent','hospital']
exclude = ['donate','~rt ','gospel','pray','?']
places = open('places.txt').read().split()


def list_on_tweet(array,tweet):
	
	for word in array:
		if word in tweet:
			return True
	

class StdOutListener(tweepy.StreamListener):
	
	i=0
	check_time = time.time()
	posted_tweets = []
	
	def on_data(self, data):
	
		csv = open('tweets.csv','a')
		self.i+=1
		tweet = json.loads(data)
		print tweet['text']
		csv.write(
			str(self.i)+'\t'+																#S.no
			str(tweet['id'])+'\t'+														#tweet id
			tweet['user']['id_str']+'\t'+												#user id
			tweet['user']['name'].replace('\t',' ').replace('\n',' ')+'\t'+				#name
			tweet['user']['location'].replace('\t',' ').replace('\n',' ')+'\t'+			#location
			tweet['text'].replace('\t',' ').replace('\n',' ')+'\t'+						#tweet
			tweet['created_at']+'\t'+													#datetime
			str(tweet['favorite_count'])+'\t'+											#favorite count
			str(tweet['retweet_count'])+'\n'											#RT count
		)
		
		if list_on_tweet(include,tweet['text'].lower()) or list_on_tweet(places,tweet['text'].lower()) and not list_on_tweet(exclude,'~'+tweet['text'].lower()) and tweet['text'] not in self.posted_tweets:
			#api.retweet(id=tweet['id'])
			self.posted_tweets.append(tweet['text'])
			print 'retweeted'
			
		
		if self.i%18000==0:
			while True:
				print time.time() - check_time
				if time.time() - check_time > 900:
					break
		
		return True

	def on_error(self, status):
		print status



def run_engine(key):
	
	tweetslist = []
	l = StdOutListener()
	auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
	auth.set_access_token(key.access_token, key.access_token_secret)
	api = tweepy.API(auth)
	
	stream = tweepy.Stream(auth, l)
	stream.filter(track=['#nepalquakerelief','#earthquakenepal','earthquake'],async = True)

key = all_keys[1]
run_engine(key)
	
