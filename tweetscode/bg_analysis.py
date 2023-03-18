from pytz import timezone
import matplotlib.pyplot as plt


def get_bar_chart(series, title, x, y, fname):
    '''
    Generate bar chart
    '''

    _, ax = plt.subplots()
    series.plot(kind='bar', ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)

    plt.savefig(fname, bbox_inches='tight')


def num_of_tweets(tweets):
    '''
    The number of Musk's tweets each year
    '''

    grouped_tweets = tweets.groupby(tweets['date'].dt.year).size()

    get_bar_chart(grouped_tweets, 'Number of Tweets each Year',
                  'Year', 'Amount', r'.\fig\Number_of_Tweets.png')


def when_musk_tweet(tweets):
    '''
    At what time of day does Musk tweet
    '''

    tweets['date'] = tweets['date'].dt.tz_convert(timezone('US/Central'))
    grouped_tweets = tweets.groupby(tweets['date'].dt.hour).size()

    get_bar_chart(grouped_tweets, 'When does Musk tweet?',
                  'Hour', 'Amount', r'.\fig\When.png')


def get_box_plot(grouped_tweets, attr, fname):
    '''
    generate box plot
    '''

    _, ax = plt.subplots()
    ax.boxplot([grouped_tweets.get_group(year)[attr]
               for year in grouped_tweets.groups.keys()], labels=grouped_tweets.groups.keys())
    ax.set_yscale('log')
    ax.set_xlabel('Year')
    ax.set_ylabel(attr)
    ax.set_title(attr + ' per Year')
    plt.savefig(fname, bbox_inches='tight')


def interaction_analysis(tweets):
    '''
    Analysis the number of likes, replies and retweets
    '''

    grouped_tweets = tweets.groupby(tweets['date'].dt.year)

    get_box_plot(grouped_tweets, 'likes_count', r'./fig/likes.png')
    get_box_plot(grouped_tweets, 'replies_count', r'./fig/replies.png')
    get_box_plot(grouped_tweets, 'retweets_count', r'./fig/retweets.png')


def background_analysis(tweets):
    '''
    generate some basic analysis of this tweets dataset   
    tweets: dataframe of tweets dataset
    '''

    num_of_tweets(tweets)
    when_musk_tweet(tweets)
    interaction_analysis(tweets)

    return
