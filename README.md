# Elon-Power
The Power of Elon Mask -- an ECE 143 Project

## Usage

1. Visit Google Trends and get your cookie
2. Open visual.ipynb
3. Paste your cookie in the second python cell
4. Run visual.ipynb

## Third Party Modules

1. matplotlib==3.7.0
2. numpy==1.24.2
3. pandas==1.5.3
4. pytrends==4.9.0
5. pytz==2022.7.1
6. requests==2.28.2
7. scipy==1.10.1
8. vaderSentiment==3.3.2\

## File Structure

1. sentiment code: contains all of the .py files related to sentiment analysis
2. stocks code: contains all of the .py files related to stocks analysis
3. stocks: contains all of the numerical data on stocks we used
4. trends code: contains all of the .py files related to google trends analysis
5. tweets code: contains all of the .py files related to basic tweet gathering, filtering, and sorting
6. tweets: contains all of the tweet data we used

## Dataset(s)

[Elon Musk Tweets (2010 - 2022) | Kaggle](https://www.kaggle.com/datasets/ayhmrba/elon-musk-tweets-2010-2021?select=2016.csv)

For additional data, the following link has details on using Twitter api for information:

https://blog.quantinsti.com/python-twitter-api/

## Proposed Solution and Real World Application

We plan to apply sentiment analysis by using NLP on twitter texts to measure their sentiment and how that translates to a real world impact factoring in tweet engagement. The real world applications of this project are that it can be used to demonstrate the effects of highly-known public figures’ social media on stocks, sentiments, etc. Companies and agents can use this for marketing purposes. Public figures can use this to view the tangible effects their posts have and determine whether or not they should post about things. 

## Project Steps

Data Gathering: We filter through Elon Musk’s tweets on a sundry of aspects, such as stocks, policies making, and people, as well as a few other sources as necessary to get the effects of those tweets. We estimate this will take 1.5 weeks.

Sentiment Analysis: Apply NLP on texts of tweets to measure sentiment (1) positive (0) neutral (-1) negative. We estimate this will take 1.5 weeks. 

Data Visualization: We plot the graphs of the stock prices, follower counts, keyword searches, etc. before and after Musk’s tweets.
 




