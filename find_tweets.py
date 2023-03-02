import pandas as pd
import numpy as np
from datetime import date,datetime
from collections import defaultdict


# timestamp = '2012-07-12'

# extract an year and set the lookup dataset path
def extract_tweets(timestamp):
    year = timestamp.split('-')[0]
    df = pd.read_csv('./tweets/'+year+'.csv')

    dates = np.array(df['date'])
    tweets = np.array(df['tweet'])


    tweet_dict = defaultdict(list)
    for i in range(len(dates)):
        temp = dates[i].split(' ')[0]
        tweet_dict[temp].append(tweets[i])
    if(timestamp in tweet_dict.keys()):
        return tweet_dict[timestamp]
    else:
        return "no tweets for this day"

if __name__== "__main__":
    print(extract_tweets(timestamp))