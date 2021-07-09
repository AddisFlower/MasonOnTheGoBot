import os
from discord.ext import commands


class CustomEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addCustomEvent', aliases=['addEvent'],
                      description='Adds a customer event to the event list created by the members of the discord server')
    async def add_custom_event(self, ctx, title, start_date, end_date, description):
        await ctx.send("test")

class Event():
    def __init__(self, bot, name, startDate, endDate, startTime, endTime, location, description):
        self.bot = bot
        self.eventName = name
        self.eventStartDate = startDate
        self.eventEndDate = endDate
        self.eventStartTime = startTime
        self.eventEndTime = endTime
        self.eventLocation = location
        self.eventDescription = description

    def getName(self):
        return self._eventTime

    def setName(self, newName):
        self._eventName = newName

    def getStartDate(self):
        return self._eventStartDate

    def setStartDate(self, newStartDate):
        self._eventStartDate = newStartDate

    def getEndDate(self):
        return self._eventEndDate

    def setEndDate(self, newEndDate):
        self._eventEndDate = newEndDate

    def getStartTime(self):
        return self._eventStartTime

    def setStartTime(self, newStartTime):
        self._eventStartTime = newStartTime

    def getEndTime(self):
        return self._eventEndTime

    def setLocation(self, newEndTime):
        self._eventEndTime = newEndTime

    def getDescription(self):
        return self._eventDescription

    def setDescription(self, newDescription):
        self._eventDescription = newDescription

def setup(bot):
    """Necessary setup function"""
    bot.add_cog(CustomEvents(bot))
