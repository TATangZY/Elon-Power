import re

def tweets_filter(tweets, kws):
    '''
    return a dataframe that contains tweets with any of the specified keywords
    '''

    filtered = tweets[tweets.tweet.str.contains('|'.join(kws), flags=re.IGNORECASE)]
    return filtered
