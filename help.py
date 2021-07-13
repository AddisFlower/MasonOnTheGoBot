from discord.ext import commands


class MasonHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        response = '**Welcome to the Mason On The Go Bot!**\n' \
                   '**Your one stop shop for weather, events, traffic, and more!**\n' \
                   '**This bot has daily notifications for the weather forecast in Fairfax and covid immunization rates in Virginia**\n' \
                   '**This bot has multiple commands**\n' \
                   '**Chose from this list of commands:**\n' \
                   '`!currentTemp [zip-code]` - returns the current temperature in the specified zip-code. ' \
                   'If a zip-code is not specified, returns the temperature in Fairfax by default\n' \
                   '`!covidImmunizationRates [state code]` - returns the current covid vaccination rates in a specified state. ' \
                   'If a 2-letter state code is not specified, returns the rates in Virginia by default.\n' \
                   '`!currentGMUEvents` - returns the current events happening in GMU\n' \
                   '`!traffic` - begins sending live notifications for traffic events in Northern Virginia according to 511northernVA.\n' \
                   '`!stopTraffic` - ends the live notification announcements for the traffic command so no new events are sent.\n\n' \
                   '**The commands below pertain toward the custom event functionality of this bot**'
        custom = '`!createEvent` - creates a custom event with the given arguments that are separated by |.\n' \
                 'Use the command like this: `!createEvent name | start date | end date | start time | end time | location | description`\n' \
                 '`!displayEvents` - returns all the created events in the discord server. \n' \
                 '`!setEventName [eventID]` - sets the name of an event in the event list with the given id.\n ' \
                 '`!setEventStartDate [eventID]` - sets the start date of an event in the event list with the given id.\n' \
                 '`!setEventEndDate [eventID]` - sets the end date of an event in the event list with the given id.\n' \
                 '`!setEventStartTime [eventID]` - sets the start time of an event in the event list with the given id.\n' \
                 '`!setEventEndTime [eventID]` - sets the end time of an event in the event list with the given id.\n' \
                 '`!setEventLocation [eventID]` - sets the location of an event in the event list with the given id.\n' \
                 '`!setEventDescription [eventID]` - sets the description of an event in the event list with the given id.\n' \
                 '`!setEventName [eventID]` - sets the name of an event in the event list with the given id.\n' \
                 '`!clearEvents ` - clears all the events in the current event list.\n' \
                 '`!removeEvent [eventID]` - removes the event with the given id from the event list.'

        await self.get_destination().send(response)
        await self.get_destination().send(custom)

    async def send_command_help(self, command):
        return self.get_destination().send(command.description)
