import discord
import json
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Help command
@bot.command(aliases=['botInfo', 'commands'])
async def info(ctx):
    response = '**This bot has multiple commands**\n' \
               '**Chose from this list of commands:**\n' \
               '`!currentTemp` - returns the current temperature in the specified zip-code. ' \
               'If a zip-code is not specified, returns the temperature in Fairfax by default\n' \
               '`!covidImmunizationRates` - returns the current covid vaccination rates in a specified state. ' \
               'If a 2-letter state code is not specified, returns the rates in Virginia by default.\n' \
               '`!currentEvents` - returns the current events happening in GMU\n'
    await ctx.send(response)

# Command for current temperature (uses OpenWeatherMap api)
# The bot uses zipcode 22030 as the location currently, we can change it later if we want
@bot.command(aliases=['currentTemp', 'currentTemperature'])
async def temp(ctx, zip_code=''):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    default = False

    # If the user doesn't specify a zip-code, the bot will give the temp for Fairfax
    if zip_code == '':
        default = True
        url = base_url + "q=22030,us&units=imperial&appid=" + API_KEY
    # Otherwise, use the zip-code that the user specified
    else:
        url = base_url + "q=" + zip_code + ",us&units=imperial&appid=" + API_KEY
    response = requests.get(url)

    # If the request was successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = main['temp']
        if default:
            temperature = "The current temperature in Fairfax is **%.2f °F**" % temp
        else:
            temperature = "The current temperature in zip-code " + zip_code + " is **%.2f° F**" % temp
        await ctx.send(temperature)
    # Otherwise, give the user a message that the request wasn't successful
    else:
        response = "Error getting temperature, try again later."
        await ctx.send(response)

# Command for covid immunization rates (uses CDC api)
# Currently using Virginia as the default location, but we can change it later
@bot.command(aliases=['covidImmunizationRates', 'vaccinationRates','percentOfPeopleVaccinated'])
async def covid(ctx, state=''):
    base_url = "https://data.cdc.gov/resource/unsk-b7fc.json?location="
    default = False

    # If the user doesn't specify a 2-letter state code after the command,
    # the bot will give the immunization rates in Virginia by default.
    if state == '':
        default = True
        url = base_url + "VA"
    # Otherwise, use the 2-letter state code that the user specified
    else:
        url = base_url + state.upper()

    # If the request was successful
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        vaccination_rate = data[0]['series_complete_pop_pct']
        if default:
            result = "The current percentage of people who are fully vaccinated in VA is **" + vaccination_rate + "%** "
        else:
            result = "The current percentage of people who are fully vaccinated in " + state.upper() + " is **" + vaccination_rate + "%** "
        await ctx.send(result)
    # Otherwise, give the user a message that the request wasn't successful
    else:
        await ctx.send('Error getting vaccination records, try again later.')

bot.run(TOKEN)
