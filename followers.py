import tweepy
import datetime

# Add your Twitter API keys and access tokens here
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Set the username and the date you want to retrieve the follower count for
username = 'your_username'
date_str = 'YYYY-MM-DD'  # replace with the date you want to retrieve the follower count for

# Convert the date string to a datetime object
date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

# Call the followers/list endpoint to retrieve the user's followers
followers = tweepy.Cursor(api.followers, screen_name=username).items()

# Initialize the follower count to zero
follower_count = 0

# Iterate through the followers and count the ones that followed the user on or before the specified date
for follower in followers:
    follower_date = datetime.datetime.strptime(follower.created_at, '%a %b %d %H:%M:%S +0000 %Y')
    if follower_date.date() <= date.date():
        follower_count += 1

# Print the follower count for the specified date
print(follower_count)
