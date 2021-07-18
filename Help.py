from discord.ext import commands


class MasonHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        response = '**Welcome to the Mason On The Go Bot!**\n' \
                   '**Your one stop shop for weather, events, traffic, and more!**\n\n' \
                   '**These are the commands that are offered by this bot:**\n' \
                   '`!currentTemp [zip-code]` - returns the current temperature in the specified zip-code. ' \
                   'If a zip-code is not specified, returns the temperature in Fairfax by default.\nExample use: `!currentTemp 90001`\n\n' \
                   '`!covidImmunizationRates [state code]` - returns the current covid vaccination rates in a specified state. ' \
                   'If a 2-letter state code is not specified, returns the rates in Virginia by default.\nExample use: `!currentImmunizationRates TX`\n\n' \
                   '`!currentGMUEvents` - returns the current events happening in GMU\n\n' \
                   '**These are the commands used to change at what time and which channel the notifications and traffic updates are sent:**\n' \
                   '`!setNotificationTime [hour] [minute]` - sets the time the user wants the two daily notifications should happen at.\nYou must input the time using military time format and omit any leading 0s.\nFor example, `!setNotificationTimeTime 23 1` would make the notifications be sent at 11:01 PM.\n\n' \
                   '`!setNotificationChannel [channel name]` - sets the channel where the notifications and traffic updates are sent.\nExample use: `!setNotificationChannel general`\n\n' \
                   '`!traffic` - begins sending live notifications for traffic events in Northern Virginia according to 511northernVA.\n' \
                   '`!stopTraffic` - ends the live notification announcements for the traffic command so no new events are sent.\n\n' \
                   '**The commands below pertain toward the custom event functionality of this bot**'
        custom = '`!createEvent` - creates a custom event with the given arguments that are separated by |.\n' \
                 'Use this format: `!createEvent [name] | [start date] | [end date] | [start time] | [end time] | [location] | [description]`\n' \
                 'Example use: `!createEvent Movie Night | 7/29/21 | 7/29/21 | 6:30 PM | 10:00 PM | University Mall Theaters | Bring your friends and family and enjoy a night out at the movies!`\n\n' \
                 '`!displayEvents` - returns all the created events in the discord server. \n\n' \
                 '`!setEventName [eventID] [newName]` - sets the name of an event in the event list with the given id.\n' \
                 'Example use: `!setEventName 1 Track`\n\n ' \
                 '`!setEventStartDate [eventID] [new start date]` - sets the start date of an event in the event list with the given id.\n' \
                 'Example use: `!setEventStartDate 2 07/30/21`\n' \
                 '`!setEventEndDate [eventID] [new end date]` - sets the end date of an event in the event list with the given id.\n' \
                 'Example use: `!setEventEndDate 2 08/02/21`\n\n' \
                 '`!setEventStartTime [eventID] [new start time]` - sets the start time of an event in the event list with the given id.\n' \
                 'Example use: `!setEventStartTime 3 7:00 AM`\n' \
                 '`!setEventEndTime [eventID] [new end time]` - sets the end time of an event in the event list with the given id.\n' \
                 'Example use: `!setEventEndTime 3 11:00 AM`\n\n' \
                 '`!setEventLocation [eventID] [new location]` - sets the location of an event in the event list with the given id.\n' \
                 'Example use: `!setEventLocation 4 RAC Center`\n\n' \
                 '`!setEventDescription [eventID] [new description]` - sets the description of an event in the event list with the given id.\n' \
                 'Example use: `!setEventDescription 5 Last competition of the year.`\n\n' \
                 '`!clearEvents ` - clears all the events in the current event list.\n' \
                 '`!removeEvent [eventID]` - removes the event with the given id from the event list.\n' \
                 'Example use: `!removeEvent 6`'

        await self.get_destination().send(response)
        await self.get_destination().send(custom)

    async def send_command_help(self, command):
        return self.get_destination().send(command.description)
