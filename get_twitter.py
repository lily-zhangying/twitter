__author__ = 'lily'

import tweepy

# get twitter application information
f = open('token.txt', 'r')
consumer_key = f.readline().strip()
consumer_secret = f.readline().strip()
access_token = f.readline().strip()
access_token_secret = f.readline().strip()
f.close()

# get authentation of twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#  search resent twitter with keyword china
resent_tweets = api.search("China")
result_file = open("result.txt", "w")
for tweet in resent_tweets:
    line = tweet.text
    result_file.write(line.encode('ascii', 'ignore') + "\n")
result_file.close()