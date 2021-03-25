import tweepy
from twittercreds import *

def login_twitter():
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret) 
    api = tweepy.API(auth)
    return api
  
def get_old_name(api):
  tweets = api.user_timeline(screen_name='NahimName', count=1, include_rts = False, tweet_mode = 'extended')
  old_name = tweets[0].full_text.encode('utf-8')
  return old_name

def get_current_name(api):
  user_id = 2467643810 # Nahim's twitter user ID. Unique for every Twitter user
  user = api.get_user(user_id)
  current_name = user.name.encode('utf-8')
  return current_name

def lambda_handler(event, context):
  api = login_twitter()
  old_name = get_old_name(api)
  current_name = get_current_name(api)
  if current_name != old_name:
      api.update_status(current_name.decode())
