# nahim-name

## About

Tracks when [@nah_im_abdulla](https://twitter.com/nah_im_abdulla) changes his screen name and tweets it out on [@NahimName](https://twitter.com/NahimName).

## Files
* `name.txt` saves the current name and rewrites when name is changed.
* `script.py` has the script for the twitter bot.
* To run the script, get API access tokens from https://developer.twitter.com/en/apps and save it in a file `twittercreds.py` as follows:

```
api_key = "xxxxxxxx"
api_secret = "xxXXXx"
access_token = "xxxx"
access_secret = "xxXXX
```

## Misc

Every Twitter user has a unique ID that remains constant even after username changes. Use this https://tweeterid.com/ to find ID for any username. This is used to extract information about a user from Twitter using the Twitter API (such as screen name in this case)

The script is scheduled to run every 15 minutes using Windows Task Scheduler.


