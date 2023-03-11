import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import pathlib

def plot_before_n_after(company_name, tweet_date, avg=10, scope=50):

    '''
    Plot the graph of the price and the volume of a company before Elon Musk tweeted.
    
    Keyword:
    company_name: the name of the comany
    tweet_date: the date that Elon Musk tweeted
    avg: the number of days that the user want to average the data
    range: the range of the scope
    '''

    assert isinstance(company_name, str)
    assert isinstance(tweet_date, str)

    fname = ""
    folder_name = './tweets/'
    if (company_name == 'tesla'):
        fname = folder_name + 'TSLA.csv'
    elif (company_name == 'tweeter'):
        fname = folder_name + 'TWTR.csv'
    elif (company_name == 'bitcoin'):
        fname = folder_name + 'BTC-USD.csv'
    elif (company_name == 'dogecoin'):
        fname = folder_name + 'DOGE-USD.csv'
    elif (company_name == 'gamestop'):
        fname = folder_name + 'GME.csv'
    
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
    query = -1
    query = df.index.get_indexer([tweet_date], method="nearest")[0]

    # calculate the scope of the data
    lhs = query - scope if query- scope > 0 else 0
    rhs = query + scope if query- scope < len(df_avg) else -1

    # grab the data from the dataframe
    volumes = pd.Series(df_avg['Volume'][lhs:rhs])
    closing_prices = pd.Series(df_avg['Adj Close'][lhs:rhs])

    # the main plot
    fig, axs = plt.subplots(2, figsize=(16,9))
    fig.suptitle('Before Musk\'s Tweet and After')

    # axis 0
    axs[0].plot(volumes.index, volumes.values, label='Volume')
    axs[0].vlines(x = df_avg.index[query], ymin = min(volumes), ymax = max(volumes.values),
            colors = 'purple',
            label = 'Musk\'s Tweet')
    axs[0].legend()
    axs[0].get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    axs[0].set_ylabel('Volume')

    # axis 1
    axs[1].plot(closing_prices.index, closing_prices.values, label='Closing Price', c='g')
    axs[1].vlines(x = df_avg.index[query], ymin = min(closing_prices.values), ymax = max(closing_prices.values),
            colors = 'purple',
            label = 'Musk\'s Tweet')
    axs[1].legend()
    axs[1].set_ylabel('Adj. Price')
