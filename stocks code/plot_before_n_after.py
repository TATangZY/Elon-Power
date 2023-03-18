import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import pathlib
import numpy as np

def plot_before_n_after(company_name, tweet_dates, avg=10, scope=50):

    '''
    Plot the graph of the price and the volume of a company before Elon Musk tweeted.
    
    Keyword:
    company_name: the name of the comany
    tweet_date: the date that Elon Musk tweeted
    avg: the number of days that the user want to average the data
    range: the range of the scope
    '''

    assert isinstance(company_name, str)
    assert isinstance(tweet_dates, list)

    fname = "./stocks/"
    if (company_name == 'tesla'):
        fname += 'TSLA.csv'
    elif (company_name == 'twitter'):
        fname += 'TWTR.csv'
    elif (company_name == 'bitcoin'):
        fname += 'BTC-USD.csv'
    elif (company_name == 'dogecoin'):
        fname += 'DOGE-USD.csv'
    elif (company_name == 'gamestop'):
        fname += 'GME.csv'
    elif (company_name == 'amazon'):
        fname += 'AMZN.csv'
    elif (company_name == 'ford'):
        fname += 'F.csv'
    elif (company_name == 'apple'):
        fname += 'AAPL.csv'
    
    if not pathlib.Path(fname).is_file():

        raise FileNotFoundError
    
    # open the csv file
    df = pd.read_csv(fname)
    
    # convert the dtype to datetime64
    df.Date = pd.to_datetime(df.Date, format='%Y-%m-%d')
    df = df.set_index('Date')

    # average the closing price and the volume
    df_avg = df[['Adj Close', 'Volume']].rolling(avg, min_periods=1).mean()

    # to make sure the query exists in the dataframe
    # since the tweet date may not be an opening day
    queries = []
    colors = []
    for tweet_date in tweet_dates:
        queries.append(df.index.get_indexer([tweet_date], method="nearest")[0])
        colors.append(np.random.rand(3,))

    # calculate the scope of the data
    lhs = min(queries) - scope if min(queries)- scope > 0 else 0
    rhs = max(queries) + scope if max(queries)- scope < len(df_avg) else -1

    # grab the data from the dataframe
    volumes = pd.Series(df_avg['Volume'][lhs:rhs])
    closing_prices = pd.Series(df_avg['Adj Close'][lhs:rhs])

    # the main plot
    fig, axs = plt.subplots(2, figsize=(16,9))
    fig.suptitle('Impact on {} Before Musk\'s Tweet and After'.format(company_name.capitalize()))
    
    # axis 0
    axs[0].plot(volumes.index, volumes.values, label='Volume')
    
    for itr, query in enumerate(queries):
        axs[0].vlines(x = df_avg.index[query], ymin = min(volumes), ymax = max(volumes.values),
            colors = colors[itr],
            label = 'Musk\'s Tweet {}'.format(itr))
    axs[0].legend()
    axs[0].set_ylabel('Volume')

    axs[1].plot(closing_prices.index, closing_prices.values, label='Closing Price', c='g')
    for itr, query in enumerate(queries):
        axs[1].vlines(x = df_avg.index[query], ymin = min(closing_prices), ymax = max(closing_prices.values),
            colors = colors[itr],
            label = 'Musk\'s Tweet {}'.format(itr))
    axs[1].legend()
    axs[1].set_ylabel('Adj. Price')
