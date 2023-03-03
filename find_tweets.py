from collections import defaultdict

import pandas as pd
import numpy as np


# extract an year and set the lookup dataset path
def extract_tweets(timestamp, df):
    '''
    This function returns the tweets for a given yyyy-mm-dd

    args:
    timestamp: a string of format 'yyyy-mm-dd'
    df: the dataframe of the entire cleaned data

    returns:
    A list of tweets if there are any tweets in the dataset on the given day
    '''
    timestamp = pd.to_datetime(timestamp).tz_localize(
        'US/Central').strftime('%Y-%m-%d')

    dates = np.array(df['date'])
    tweets = np.array(df['tweet'])

    tweet_dict = defaultdict(list)
    for i, date in enumerate(dates):
        # get the timestamp of the date
        date_ts = date.to_period(freq='D').strftime('%Y-%m-%d')
        tweet_dict[date_ts].append(tweets[i])

    if (timestamp in tweet_dict.keys()):
        return tweet_dict[timestamp]
    else:
        print("no tweets for this day")
        return []
