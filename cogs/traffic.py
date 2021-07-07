import os
import os
from datetime import time

import tweepy
from discord.ext import commands

API_KEY = os.getenv('T_API_Key')
API_SECRET_KEY = os.getenv('T_API_Secret_Key')
ACCESS_TOKEN = os.getenv('T_Access_Token')
ACCESS_TOKEN_SECRET = os.getenv('T_Access_Token_Secret')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)


class Traffic(commands.Cog):
    """ This is a cog with the traffic updates functionality."""

    def __init__(self, bot):
        self.bot = bot

    # Command for current traffic updates
    @commands.command(name='trafficTest', aliases=['traffic'],
                      description='Sends the latest traffic event')
    async def today(self, ctx):
        username = '511northernva'
        count = 1

        try:
            # Creation of query method using parameters
            tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)

            # Pulling information from tweets iterable object
            tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
            text = tweets_list.pop(0).pop(2)
            x = text.split("https:")
            message = x.pop(0)
            await ctx.send(message)

        except BaseException as e:
            print('failed on_status,', str(e))
            time.sleep(3)

def setup(bot):
    """Necessary setup function"""
    bot.add_cog(Traffic(bot))
