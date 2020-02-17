import tweepy
from twittercreds import * # Twitter API keys are stored in twittercreds.py
from datetime import datetime

# get old name from file

with open('name.txt') as f:
	old_name = f.read()

# get current name from twitter

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret) 
api = tweepy.API(auth)
user_id = 2467643810 # Nahim's Twitter user ID
user = api.get_user(user_id)
current_name = user.name

# post if changed

if current_name != old_name:
	tweet_txt = f'Nahim has changed his display name to {current_name}'
	api.update_status(tweet_txt)

	# update name file

	with open('name.txt', 'w+') as f:
		f.write(current_name)

# write log

now = datetime.now()
current_time = now.strftime("%Y/%m/%d %I:%M %p")

with open(f'log.csv', 'a+') as f:
	f.write(f'{current_time},{old_name},{current_name}\n')
