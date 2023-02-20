import os
import zipfile
from pytz import timezone

from pandas import read_csv, concat, to_datetime

# download from https://www.kaggle.com/datasets/ayhmrba/elon-musk-tweets-2010-2021
DATASET_NAME = 'archive.zip'


def read_tweets():
    '''
    Read tweets dataset to dataframe
    '''

    tweets_list = []
    for root, _, file_list in os.walk('tweets'):
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

    # drop columns where all values are NaN
    tweets_df.dropna(axis=1, how='all', inplace=True)
    # drop duplicate tweets
    tweets_df.drop_duplicates(subset=['id'], inplace=True)

    return tweets_df


def unzip_dataset():
    '''
    unzip dataset when necessary
    '''
    if not os.path.exists(r'./tweets/2010.csv'):
        with zipfile.ZipFile(DATASET_NAME, 'r') as zip_ref:
            zip_ref.extractall('./tweets/')
            print("Dataset upzipped")


def __main__():
    unzip_dataset()

    tweets_df = read_tweets()


__main__()
