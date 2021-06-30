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

API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')
WHEN = time(7, 0, 0)  # Time for the daily forecast notification


class Weather(commands.Cog):
    """ This is a cog with the currentTemp command and daily weather notification background task."""
    current_temp_base_url = ''
    forecast_base_url = ''

    def __init__(self, bot):
        self.bot = bot
        self.current_temp_base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.forecast_base_url = "https://api.openweathermap.org/data/2.5/onecall?lat=38.8308&lon=-77.3075&exclude=current,minutely,hourly,alerts&units=imperial&appid=" + API_KEY
        self.bot.loop.create_task(self.timer())

    # Command for current temperature (uses OpenWeatherMap api)
    # The bot uses zipcode 22030 as the location currently, we can change it later if we want
    @commands.command(name='currentTemp', aliases=['currentTemperature'],
                      description='Sends the current temperature in the specified zip-code. If a zip-code is not specified, returns the temperature in Fairfax by default.')
    async def current_temp(self, ctx, zip_code=''):
        default = False

        # If the user doesn't specify a zip-code, the bot will give the temp for Fairfax
        if zip_code == '':
            default = True
            url = self.current_temp_base_url + "q=22030,us&units=imperial&appid=" + API_KEY
        # Otherwise, use the zip-code that the user specified
        else:
            url = self.current_temp_base_url + "q=" + zip_code + ",us&units=imperial&appid=" + API_KEY
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

    async def timer(self):
        """Function that helps time the notification so that it occurs every day at 7:00 AM"""
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
            await self.daily_forecast_notification()
            tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
            seconds = (tomorrow - now).total_seconds()
            await asyncio.sleep(seconds)

    async def daily_forecast_notification(self):
        """Basic daily weather notification (using GMU as the location for weather collection)"""
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(int(CHANNEL_ID))
        response = requests.get(self.forecast_base_url)

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


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(Weather(bot))
