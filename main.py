import os
import zipfile
from pytz import timezone

from pandas import read_csv, concat, to_datetime
from bg_analysis import background_analysis
from sentiment import sentimentAnalysis

# download from https://www.kaggle.com/datasets/ayhmrba/elon-musk-tweets-2010-2021
DATASET_NAME = 'archive.zip'
TWEETS_FOLDER = './archive/'

def wash(tweets_df):
    '''
    Essential data wash
    '''

    # drop columns where all values are NaN
    tweets_df.dropna(axis=1, how='all', inplace=True)
    # drop duplicate tweets
    tweets_df.drop_duplicates(subset=['id'], inplace=True)

    # merge nlikes, nreplies, nretweets and likes_count, replies_count, retweets_count
    tweets_df.loc[:, ['nlikes', 'nreplies', 'nretweets']] = tweets_df.loc[:, [
        'nlikes', 'nreplies', 'nretweets']].fillna(0)
    tweets_df.loc[:, ['likes_count', 'replies_count', 'retweets_count']] = tweets_df.loc[:, [
        'likes_count', 'replies_count', 'retweets_count']].fillna(0)
    tweets_df['likes_count'] += tweets_df['nlikes']
    tweets_df['replies_count'] += tweets_df['nreplies']
    tweets_df['retweets_count'] += tweets_df['nretweets']

    tweets_df = tweets_df.drop(['nlikes', 'nreplies', 'nretweets'], axis=1)

    return tweets_df


def read_tweets():
    '''
    Read tweets dataset to dataframe
    '''

    tweets_list = []
    for root, _, file_list in os.walk(TWEETS_FOLDER):
        for file in file_list:
            # these two file is different from others
            if file not in ['2021.csv', '2022.csv']:
                cur_tweets = read_csv(os.path.join(
                    root, file), parse_dates=['date'])
                cur_tweets = cur_tweets.drop(
                    cur_tweets.columns[0], axis=1)  # drop the col for counting
                cur_tweets['date'] = cur_tweets['date'].dt.tz_localize(
                    timezone('UTC'))  # set date to UTC
            else:
                cur_tweets = read_csv(os.path.join(root, file))
                cur_tweets['date'] = cur_tweets.apply(
                    lambda r: r['date'] + ' ' + r['time'], axis=1)  # concat time to date
                cur_tweets['date'] = to_datetime(cur_tweets['date'])
                cur_tweets['date'] = cur_tweets['date'].dt.tz_localize(
                    timezone('Asia/Dubai'))  # set date to UTC +4

            tweets_list.append(cur_tweets)

    tweets_df = concat(tweets_list, axis=0, ignore_index=True)
    tweets_df['date'] = to_datetime(tweets_df['date'], utc=True)

    tweets_df = wash(tweets_df)

    return tweets_df


def unzip_dataset():
    '''
    unzip dataset when necessary
    '''

    if not os.path.exists(os.path.join(TWEETS_FOLDER, '2010.csv')):
        with zipfile.ZipFile(DATASET_NAME, 'r') as zip_ref:
            zip_ref.extractall(TWEETS_FOLDER)
            print("Dataset upzipped")


def __main__():
    unzip_dataset()

    tweets_df = read_tweets()

    os.makedirs(os.path.dirname('./fig/'), exist_ok=True)
    background_analysis(tweets_df)
    tweets_df = sentimentAnalysis(tweets_df)

__main__()
