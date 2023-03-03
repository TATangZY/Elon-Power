import re
from collections import defaultdict

from pandas import DataFrame


def tweets_filter(tweets, kws):
    '''
    return a dataframe that contains tweets with any of the specified keywords
    '''

    filtered = tweets[tweets.tweet.str.contains(
        '|'.join(kws), flags=re.IGNORECASE)]
    return filtered


def get_tweets_with_topic(tweets_df):
    '''
    return: a dictionary that the keys are topics and values 
            are a Dataframes containing all the rows related to that topic
    '''

    topic_dict = defaultdict(DataFrame)

    # Add topic and its keywords (ignore case) here

    # Tesla
    tesla_kws = ['tesla', 'model s', 'model 3', 'model x', 'model y',]
    topic_dict['tesla'] = tweets_filter(tweets_df, tesla_kws)

    # Bitcoin
    bit_kws = ['bitcoin',]
    topic_dict['bitcoin'] = tweets_filter(tweets_df, bit_kws)

    # Dogecoin
    doge_kws = ['dogecoin',]
    topic_dict['dogecoin'] = tweets_filter(tweets_df, doge_kws)

    # Twitter
    tw_kws = ['twitter',]
    topic_dict['twitter'] = tweets_filter(tweets_df, tw_kws)

    return topic_dict
