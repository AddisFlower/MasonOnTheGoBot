import discord
import json
import requests
import os
from dotgitignore import load_dotgitignore
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta, time

API_KEY = os.getgitignore('API_Key')
API_SECRET_KEY = os.getgitignore('API_Secret_Key')
ACCESS_TOKEN = os.getgitignore('Access_Token')
ACCESS_TOKEN_SECRET = os.getgitignore('Access_Token_Secret')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

class Traffic(commands.Cog):
    """ This is a cog with the currentTemp command and daily weather notification background task."""

    def __init__(self, bot):
        self.bot = bot
        self.username = '511statewideva'
        self.count = 1

    # Command for current event list
    @commands.command(name='trafficTest', aliases=['traffic'],
                      description='Sends the latest traffic event')
    async def today(self, ctx):
        
        try:     
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
 
        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        
 
        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list)
        except BaseException as e:
             ctx.send('failed on_status,',str(e))
             time.sleep(3)
    
        for tweet in tweets_list: 
            text = tweet.full_text
            ctx.send(text)

def setup(bot):
    """Necessary setup function"""
    bot.add_cog(Traffic(bot))
