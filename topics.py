import re
from collections import defaultdict

from pandas import DataFrame

KW_DICT = {}
tesla_kws = ['tesla', 'model s', 'model 3', 'model x', 'model y',]
bit_kws = ['bitcoin',]
doge_kws = ['dogecoin',]
tw_kws = ['twitter',]
ford_kws = ['ford', 'mustang', 'mach-e', 'F-150']
KW_DICT['tesla'] = tesla_kws
KW_DICT['bitcoin'] = bit_kws
KW_DICT['dogecoin'] = doge_kws
KW_DICT['twitter'] = tw_kws
KW_DICT['ford'] = ford_kws

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
    topic_dict['tesla'] = tweets_filter(tweets_df, tesla_kws)

    # Bitcoin
    topic_dict['bitcoin'] = tweets_filter(tweets_df, bit_kws)

    # Dogecoin
    topic_dict['dogecoin'] = tweets_filter(tweets_df, doge_kws)

    # Twitter
    topic_dict['twitter'] = tweets_filter(tweets_df, tw_kws)

    topic_dict['ford'] = tweets_filter(tweets_df, ford_kws)

    return topic_dict
