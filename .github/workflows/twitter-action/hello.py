import os

TWITTER_APP_KEY = os.environ["TWITTER_APP_KEY"]
TWITTER_APP_SECRET = os.environ["TWITTER_APP_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

if TWITTER_APP_KEY:
    print("Got app key")
if TWITTER_APP_SECRET:
    print("Got app secret")
if ACCESS_TOKEN:
    print("Got access token")
if ACCESS_TOKEN_SECRET:
    print("Got access token secret")
