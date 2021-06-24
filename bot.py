import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author.bot or message.author == client.user:
        return
    if message.content.startswith('!help'):
        response = '**This bot has multiple commands**\n' \
                   '**Chose from this list of commands:**\n' \
                   '`!currentTemperature` - returns the current temperature in Fairfax\n' \
                   '`!covidImmunizationRates` - returns the current covid vaccination rates in a specified state ' \
                   '(Virginia is the default option) \n' \
                   '`!currentEvents` - returns the current events happening in GMU\n' \
                   '`!currentTempAtLocation` returns the temperature at the specified location\n'

        await message.channel.send(response)
client.run(TOKEN)