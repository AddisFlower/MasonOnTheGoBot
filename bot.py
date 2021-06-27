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


# Commands
@client.event
async def on_message(message):
    # Dummy if statement to make sure the bot doesn't respond to itself
    if message.author.bot or message.author == client.user:
        return
    # Help command
    if message.content.startswith('!help'):
        response = '**This bot has multiple commands**\n' \
                   '**Chose from this list of commands:**\n' \
                   '`!currentTemp` - returns the current temperature in the specified zip-code.\n' \
                   'If no zip-code is specified, returns the temperature in Fairfax' \
                   '`!covidImmunizationRates` - returns the current covid vaccination rates in a specified state ' \
                   '(Virginia is the default option) \n' \
                   '`!currentEvents` - returns the current events happening in GMU\n'
        await message.channel.send(response)

    # Command for current temperature in fairfax (uses OpenWeatherMap api)
    # The bot uses zipcode 22030 as the location currently, we can change it later if we want
    if message.content.startswith('!currentTemp'):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        ZIP_CODE = ''
        default = False
        # If the user doesn't specify a zip-code, the bot will give the temp for Fairfax
        if message.content == '!currentTemp':
            default = True
            URL = BASE_URL + "q=22030,us&units=imperial&appid=" + API_KEY
        # Otherwise, use the zip-code that the user specified
        else:
            list = message.content.split()
            ZIP_CODE = list[1]
            URL = BASE_URL + "q=" + ZIP_CODE + ",us&units=imperial&appid=" + API_KEY
        response = requests.get(URL)

        # If the request was successful
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temp = main['temp']
            if default:
                temperature = "The current temperature in Fairfax is **%.2f °F**" % temp
            else:
                temperature = "The current temperature in zip-code " + ZIP_CODE + " is **%.2f °F**" %temp
            await message.channel.send(temperature)
        # Otherwise, give the user a message that the request wasn't successful
        else:
            response = "Error getting temperature, try again later."
            await message.channel.send(response)


client.run(TOKEN)
