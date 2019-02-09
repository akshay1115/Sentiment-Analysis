import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class TwitterClient(object): 
	def __init__(self): 
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'rsltUXPjjPB9wZzkMijOhcjiB'
		consumer_secret = 'dsqX8qHZyViIgRD1DOujdFL7P0Lh2tFFL897OlSIYSl0tZdGc2'
		access_token = '1065036280172437504-vzRa8idv1XFZveeQEUWOyAii2dY7Ct'
		access_token_secret = 'UYawwqGnRkz0IcfMgSj1n131flOD9aMXCTB7GFWLZohwi'

		# attempt authentication 
		try: 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("Error: Authentication Failed") 

	def clean_tweet(self, tweet): 
		''' 
		function to clean tweet text
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

	def get_tweet_sentiment(self, tweet): 
		''' 
		function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		'''
		analysis = TextBlob(self.clean_tweet(tweet)) 
		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 10): 
		''' 
		function to fetch tweets and parse them. 
		''' 
		tweets = [] 

		try: 
			fetched_tweets = self.api.search(q = query, count = count) 

			for tweet in fetched_tweets: 
				parsed_tweet = {} 

				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				if tweet.retweet_count > 0: 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
					tweets.append(parsed_tweet) 

			return tweets 

		except tweepy.TweepError as e: 
			print("Error : " + str(e)) 

def main(): 
	# creating object of TwitterClient Class 
	api = TwitterClient() 
	tweets = api.get_tweets(query = 'Justin Trudeau', count = 200) 
	# picking positive tweets from tweets 
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 

	# picking negative tweets from tweets 
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
	
	# printing first 5 positive tweets 
	print("\n\nPositive tweets:") 
	for tweet in ptweets[:10]: 
		print(tweet['text']) 

	# printing first 5 negative tweets 
	print("\n\nNegative tweets:") 
	for tweet in ntweets[:10]: 
		print(tweet['text'])

if __name__ == "__main__": 
	# calling main function 
	main() 
