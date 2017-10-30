import unittest
import tweepy
import requests
import json

## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Thursday 6-7 PM
## Any names of people you worked with on this assignment: Harrison Dvoor and I worked together on #4

## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.

## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing

## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points

consumer_key = "6g7GK7UX2UMtMMo1dd40Ecxry" 
consumer_secret = "PQfhOtNubWXeY9zrOiBucpppL9EApLgQb51Oc8ugbxsci21IXO"
access_token = "920733501074366465-FyjyIKjU58FEO9n7BHt27WT2hImyTlf"
access_token_secret = "8NUtxLRZpAmiOs87YNP6Di3s8KUOEtiOSv0XqTYtAhoQH"

## Set up your authentication to Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.

CACHE_FNAME = 'Cache_HW7.json' 						## I am making a cache file and naming it "Cache_HW7" (and saving that as a variable CACHE_FNAME)

try:
    cache_file = open(CACHE_FNAME, 'r') 		## I am opening the cache file (via the variable CACHE_FNAME)
    cache_contents = cache_file.read()				## and reading the data of this cache file into a string
    CACHE_DICTION = json.loads(cache_contents)			## I am loading this data of the cache file into a python object
    cache_file.close()								## and am now closing the cache file
except:
    CACHE_DICTION = {}								## if the above actions don't run then I want the data to go somewhere (this dictionary)

## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is. 

def get_Twitter_Data(my_var):
	if my_var in CACHE_DICTION:
		print ("Data found in cache file")		## return all the contents associated with search item my_var, if my_var is found in cache file (has already been cached)
		return CACHE_DICTION[my_var]
	else:
		print("Requesting new data...")				## if my_var has not been cached yet
		api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
		tweet_search = api.search(my_var)
		tweet_data = {}

		for specific_tweet in tweet_search['statuses']:
			tweet_data[specific_tweet['text']] = specific_tweet['created_at']

		CACHE_DICTION[my_var] = tweet_data
		writing_file = open(CACHE_FNAME, 'w')
		writing_file.write(json.dumps(CACHE_DICTION))
		writing_file.close()

	return tweet_data

## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!

tweet_input = input("Enter Twitter search phrase - ")
twitter_data = get_Twitter_Data(tweet_input)

## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.

my_count = 0
for key in twitter_data.keys():
	if (my_count < 5):
		print ("Text: " + key)
		print ("Created At: " + key)
		print ("\n")
		my_count = my_count + 1







