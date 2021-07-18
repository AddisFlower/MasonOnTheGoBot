import asyncio
import os
from datetime import datetime, timedelta, time
import requests
from discord.ext import commands
from bot import channel_id


API_KEY = os.getenv('API_KEY')
WHEN = time(7, 0, 0)  # Time for the daily covid notification


class Covid(commands.Cog):
    """ This is a cog with the covidImmunizationRates command and daily covid immunization notification background task(not yet implemented)."""
    base_url = ''
    notification_base_url = ''

    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://data.cdc.gov/resource/unsk-b7fc.json?location="
        self.bot.loop.create_task(self.timer())

    @commands.command(name='covidImmunizationRates', aliases=['covid', 'vaccinationRates', 'percentOfPeopleVaccinated'],
                      decription='Sends the current covid vaccination rates in a specified state. If a 2-letter state code is not specified, returns the rates in Virginia by default')
    async def current_rates(self, ctx, state=''):
        """Command for covid immunization rates (uses CDC api). Currently using Virginia as the default location, but we can change it later."""
        default = False

        # If the user doesn't specify a 2-letter state code after the command,
        # the bot will give the immunization rates in Virginia by default.
        if state == '':
            default = True
            url = self.base_url + "VA"
        # Otherwise, use the 2-letter state code that the user specified
        else:
            url = self.base_url + state.upper()

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
            await self.daily_covid_notification()
            tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
            seconds = (tomorrow - now).total_seconds()
            await asyncio.sleep(seconds)

    async def daily_covid_notification(self):
        """Basic daily weather notification (using GMU as the location for weather collection)"""
        url = self.base_url + "VA"
        channel = self.bot.get_channel(channel_id)

        # If the request was successful
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vaccination_rate = data[0]['series_complete_pop_pct']
            result = "\nHello! This is your MasonOnTheGo Bot with your daily morning covid report.\n\n "
            result += "The current percentage of people who are fully vaccinated in VA is **" + vaccination_rate + "%** "
            await channel.send(result)
        # Otherwise, give the user a message that the request wasn't successful
        else:
            await channel.send('Error providing daily covid notification.')


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(Covid(bot))
