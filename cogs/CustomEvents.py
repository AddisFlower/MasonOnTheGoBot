import os
from discord.ext import commands


class CustomEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addCustomEvent', aliases=['addEvent'],
                      description='Adds a customer event to the event list created by the members of the discord server')
    async def add_custom_event(self, ctx, title, start_date, end_date, description):
        await ctx.send("test")

class Event(commands.Cog):
    @commands.command(name='addCustomEvent', aliases=['addEvent'], description='Adds custom event to list of events.')
    def __init__(self, bot, name, time, location, description):
        self.bot = bot
        self.eventName = name
        self.eventTime = time
        self.eventLocation = location
        self.eventDescription = description

    def getName(self):
        return self._eventTime

    def setName(self, newName):
        self._eventName = newName

    def getTime(self):
        return self._eventTime

    def setTime(self, newTime):
        self._eventTime = newTime

    def getLocation(self):
        return self._eventLocation

    def setLocation(self, newLocation):
        self._eventLocation = newLocation

    def getDescription(self):
        return self._eventDescription

    def setDescription(self, newDescription):
        self._eventDescription = newDescription

def setup(bot):
    """Necessary setup function"""
    bot.add_cog(CustomEvents(bot))
