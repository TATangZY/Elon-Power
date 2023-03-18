import pandas as pd
def imp_tweets_sentiment(infl_tweets_id, tweets_df):
    '''
    takes a list of tweet id's and returns the tweets as a dataframe
    also prints the tweet sentiment breakdown.

    Input:
    infl_tweets_id: list

    Return:
    infl_tweets_df: pd dataframe
    '''
    assert isinstance(infl_tweets_id,list), "Input not a list"
    infl_tweets_df = pd.DataFrame()
    for tweet in infl_tweets_id:
        row = tweets_df.loc[tweets_df['id'] == tweet]
        infl_tweets_df = pd.concat([row,infl_tweets_df.loc[:]]).reset_index(drop=True)
    sentiment_sum = 0
    count = 0
    positive_sentiment = 0
    negative_sentiment = 0
    neutral_sentiment = 0 
    for x in infl_tweets_df.loc[:,'tweet_sentiment']:
        print(x)
        if x == 0:
            neutral_sentiment += 1 
        if x>0:
            positive_sentiment += 1
        if x<0:
            negative_sentiment += 1
        count += 1
        sentiment_sum += x 
    print(negative_sentiment,"negative sentiment tweets")
    print(positive_sentiment,"positive sentiment tweets")
    print(neutral_sentiment, "neutral sentiment tweets")
    avg_sentiment = sentiment_sum/count
    if avg_sentiment == 0:
        print("average sentiment is neutral", avg_sentiment)
    if avg_sentiment>0:
        print("average sentiment is positive", avg_sentiment)
    if avg_sentiment<0:
        negative_sentiment += 1
        print("average sentiment is negative", avg_sentiment)
    return infl_tweets_df
