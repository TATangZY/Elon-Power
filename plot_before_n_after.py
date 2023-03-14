import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import pathlib

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
    fig.suptitle('Impact on {} Before Musk\'s Tweet and After'.format(company_name.capitalize()))
    
    
    
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    
    

    # axis 0
    textstr = '\n'.join((
    r'$\delta_{one} = %.2f$' % ((df_avg['Volume'][query] - df_avg['Volume'][query-1])/df_avg['Volume'][query], ),
    r'$\delta_{three} = %.2f$' % ((df_avg['Volume'][query+3] - df_avg['Volume'][query])/df_avg['Volume'][query], )))
    axs[0].text(0.15, 0.95, textstr, transform=axs[0].transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    axs[0].plot(volumes.index, volumes.values, label='Volume')
    axs[0].vlines(x = df_avg.index[query], ymin = min(volumes), ymax = max(volumes.values),
            colors = 'purple',
            label = 'Musk\'s Tweet')
    axs[0].legend()
    axs[0].get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    axs[0].set_ylabel('Volume')

    # axis 1
    textstr = '\n'.join((
    r'$\delta_{one} = %.2f$' % ((df_avg['Adj Close'][query] - df_avg['Adj Close'][query-1])/df_avg['Adj Close'][query], ),
    r'$\delta_{three} = %.2f$' % ((df_avg['Adj Close'][query+3] - df_avg['Adj Close'][query])/df_avg['Adj Close'][query], )))
    axs[1].text(0.15, 0.95, textstr, transform=axs[1].transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    axs[1].plot(closing_prices.index, closing_prices.values, label='Closing Price', c='g')
    axs[1].vlines(x = df_avg.index[query], ymin = min(closing_prices.values), ymax = max(closing_prices.values),
            colors = 'purple',
            label = 'Musk\'s Tweet')
    axs[1].legend()
    axs[1].set_ylabel('Adj. Price')