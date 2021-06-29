import discord
import json
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta, time

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')  # Discord channel where the notification will be sent (will change this later to be modifiable by the user
WHEN = time(7, 0, 0) # Time for the weather notification

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    bot.loop.create_task(timer())
    print(f'{bot.user} has connected to Discord!')

# Basic daily weather notification (using GMU as the location for weather collection)
async def daily_weather_notification():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(CHANNEL_ID))
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat=38.8308&lon=-77.3075&exclude=current,minutely,hourly,alerts&units=imperial&appid=" + API_KEY
    response = requests.get(base_url)

    # If the request was successful
    if response.status_code == 200:
        data = response.json()
        daily = data['daily'][0]
        temp_values = daily['temp']
        feels_values = daily['feels_like']
        day_temp = temp_values['day']
        night_temp = temp_values['night']
        day_feels = feels_values['day']
        night_feels = feels_values['night']
        humidity = daily['humidity']
        weather = daily['weather'][0]
        weather_description = weather['description']
        result = "Hello! This is your MasonOnTheGo Bot with your daily weather report.\n\n "
        result += "The temperature in Fairfax during the day today will be **%.2f °F**.\n" % day_temp
        result += "However, it will feel like it is **%.2f °F**.\n\n" % day_feels
        result += "The temperature in Fairfax during the night today will be **%.2f °F**.\n" % night_temp
        result += "However, it will feel like it is **%.2f °F**.\n\n" % night_feels
        result += "The average humidity today is **%.0f%%**.\n\n" % humidity
        result += "Also, there will be " + weather_description + " today. Be well prepared!"
        await channel.send(result)
    else:
        await channel.send('Error providing daily weather notification.')

# Function that helps to time the notification so that it occurs every day at 7:00 AM
async def timer():
    now = datetime.now()
    if now.time() > WHEN:
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()
        await asyncio.sleep(seconds)
    while True:
        now = datetime.now()
        target_time = datetime.combine(now.date(), WHEN)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)
        await daily_weather_notification()
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()
        await asyncio.sleep(seconds)


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
