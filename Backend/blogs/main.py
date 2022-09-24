# extract tweets from twitter api
# and save them to a csv file

import tweepy
import csv
import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords


# Twitter API credentials
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# function to extract tweets
def get_tweets(username):

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)

        # Empty Array
        tmp=[]

        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:

            # Appending tweets to the empty array tmp
            tmp.append(j)

        # Printing the tweets
        print(tmp)

        # return array of tweets
        return tmp

# Driver code
if __name__ == '__main__':

        # Here goes the twitter handle for the user
        # whose tweets are to be extracted.
        tweets = get_tweets("realDonaldTrump")

        # printing the tweets
        print(tweets)

# save tweets to a csv file
with open('tweets.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['tweets'])
    writer.writerows(tweets)

# read csv file
df = pd.read_csv('tweets.csv')
df.head()

# remove punctuation
df['tweets'] = df['tweets'].str.replace('[^\w\s]','')
df.head()

# remove numbers
df['tweets'] = df['tweets'].str.replace('\d+', '')
df.head()

# remove stopwords
stop = stopwords.words('english')
df['tweets'] = df['tweets'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
df.head()

# remove short words
df['tweets'] = df['tweets'].apply(lambda x: " ".join(x for x in x.split() if len(x)>3))
df.head()

# remove urls
df['tweets'] = df['tweets'].str.replace('http\S+|www.\S+', '', case=False)
df.head()

# remove mentions
df['tweets'] = df['tweets'].str.replace('@\S+', '', case=False)
df.head()

# remove hashtags
df['tweets'] = df['tweets'].str.replace('#\S+', '', case=False)
df.head()

# remove emojis
df['tweets'] = df['tweets'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df.head()

# remove retweets
df['tweets'] = df['tweets'].str.replace('RT', '', case=False)
df.head()

# remove extra spaces
df['tweets'] = df['tweets'].str.replace('\s+', ' ', case=False)
df.head()



# convert to lower case
df['tweets'] = df['tweets'].str.lower()
df.head()

# remove punctuation
df['tweets'] = df['tweets'].str.replace('[^\w\s]','')
df.head()

