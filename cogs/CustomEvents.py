import os
from discord.ext import commands


class CustomEvents(commands.Cog):
    event_list = []

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addCustomEvent', aliases=['addEvent'],
                      description='Adds a customer event to the event list created by the members of the discord server')
    async def add_custom_event(self, ctx, name, startDate, endDate, startTime, endTime, location, description):
        event = Event(name, startDate, endDate, startTime, endTime, location, description)
        self.event_list.append(event)
        await ctx.send("Event added!")


class Event:
    def __init__(self, name, startDate, endDate, startTime, endTime, location, description):
        self.eventName = name
        self.eventStartDate = startDate
        self.eventEndDate = endDate
        self.eventStartTime = startTime
        self.eventEndTime = endTime
        self.eventLocation = location
        self.eventDescription = description

    def getName(self):
        return self.eventName

    def setName(self, newName):
        self.eventName = newName

    def getStartDate(self):
        return self.eventStartDate

    def setStartDate(self, newStartDate):
        self.eventStartDate = newStartDate

    def getEndDate(self):
        return self.eventEndDate

    def setEndDate(self, newEndDate):
        self.eventEndDate = newEndDate

    def getStartTime(self):
        return self.eventStartTime

    def setStartTime(self, newStartTime):
        self.eventStartTime = newStartTime

    def getEndTime(self):
        return self.eventEndTime

    def setLocation(self, newEndTime):
        self.eventEndTime = newEndTime

    def getDescription(self):
        return self.eventDescription

    def setDescription(self, newDescription):
        self.eventDescription = newDescription


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(CustomEvents(bot))
