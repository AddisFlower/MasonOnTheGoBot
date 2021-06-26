import discord
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#Commands
@client.event
async def on_message(message):
    # Dummy if statement to make sure the bot doesn't respond to itself
    if message.author.bot or message.author == client.user:
        return
    # Help command
    if message.content.startswith('!help'):
        response = '**This bot has multiple commands**\n' \
                   '**Chose from this list of commands:**\n' \
                   '`!currentTemp` - returns the current temperature in Fairfax\n' \
                   '`!covidImmunizationRates` - returns the current covid vaccination rates in a specified state ' \
                   '(Virginia is the default option) \n' \
                   '`!currentEvents` - returns the current events happening in GMU\n' \
                   '`!currentTempAtLocation` returns the temperature at the specified location\n'
        await message.channel.send(response)
    # Command for current temperature in fairfax (uses OpenWeatherMap api)
    # The bot uses zipcode 22152 as the location currently, we can change it later if we want
    if message.content.startswith('!currentTemp'):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        URL = BASE_URL + "q=22152,us&units=imperial&appid=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temp = main['temp']
            temperature = "The current temperature in Fairfax is **%.2f °F**" %temp
            await message.channel.send(temperature)
        else:
            print("Error in HTTP request")
client.run(TOKEN)