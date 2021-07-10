import os
import asyncio
from datetime import time
import tweepy
from discord.ext import commands, tasks

API_KEY = os.getenv('T_API_Key')
API_SECRET_KEY = os.getenv('T_API_Secret_Key')
ACCESS_TOKEN = os.getenv('T_Access_Token')
ACCESS_TOKEN_SECRET = os.getenv('T_Access_Token_Secret')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

CHANNEL_ID = os.getenv('CHANNEL_ID')


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
        channel = self.bot.get_channel(int(CHANNEL_ID))
        tweet_id = -1
        while True:
            tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)
            tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
            tweet_info = tweets_list.pop(0)
            temp_id = tweet_info.pop(1)
            if tweet_id != temp_id:
                tweet_id = temp_id
                text = tweet_info.pop(1)
                x = text.split("https:")
                message = x.pop(0)
                await channel.send(message)
            await asyncio.sleep(10)


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(Traffic(bot))
