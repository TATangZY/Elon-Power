from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentimentAnalysis(tweets_df):
    '''
    append a sentiment col to the dataframe
    score < 0 negative
    score = 0 neutral
    score > 0 positive
    '''
    analyzer = SentimentIntensityAnalyzer()
    tweets = tweets_df["tweet"]
    tweet_sentiment = []
    for _, tweet in enumerate(tweets):
        vs = analyzer.polarity_scores(tweet)
        tweet_sentiment.append(vs['compound'])
    tweets_df['tweet_sentiment'] = tweet_sentiment

    return tweets_df
