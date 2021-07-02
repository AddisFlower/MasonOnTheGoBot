import discord
import json
import requests
import os
from os import listdir
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta, time
from help import MasonHelpCommand

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv(
    'CHANNEL_ID')  # Discord channel where the notification will be sent (will change this later to be modifiable by the user
WHEN = time(7, 0, 0)  # Time for the weather notification

bot = commands.Bot(command_prefix='!', help_command=MasonHelpCommand())

if __name__ == '__main__':
    """Loads the cogs from the './cogs' folder."""

    for cog in listdir('./cogs'):
        if cog.endswith('.py'):
            bot.load_extension(f'cogs.{cog[:-3]}')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


bot.run(TOKEN)
