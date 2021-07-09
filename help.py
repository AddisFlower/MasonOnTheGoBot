from discord.ext import commands


class MasonHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        response = '**This bot has multiple commands**\n' \
                   '**Chose from this list of commands:**\n' \
                   '`!currentTemp` - returns the current temperature in the specified zip-code. ' \
                   'If a zip-code is not specified, returns the temperature in Fairfax by default\n' \
                   '`!covidImmunizationRates` - returns the current covid vaccination rates in a specified state. ' \
                   'If a 2-letter state code is not specified, returns the rates in Virginia by default.\n' \
                   '`!currentGMUEvents` - returns the current events happening in GMU\n\n' \
                   '**The commands below pertain toward the custom event functionality of this bot**\n' \
                   '`!createEvent` - creates a custom event with the given arguments that are separated by |.\n' \
                   'Use the command like this: `!createEvent name | start date | end date | start time | end time | location | description`\n' \
                   '`!displayEvents` - returns all the created events in the discord server. \n' \
                   '`!setEventName` - sets the name of an event in the event list with the given id.\n ' \
                   '`!setEventStartDate` - sets the start date of an event in the event list with the given id.\n' \
                   '`!setEventEndDate` - sets the end date of an event in the event list with the given id.\n' \
                   '`!setEventStartTime` - sets the start time of an event in the event list with the given id.\n' \
                   '`!setEventEndTime` - sets the end time of an event in the event list with the given id.\n' \
                   '`!setEventLocation` - sets the location of an event in the event list with the given id.\n' \
                   '`!setEventDescription` - sets the description of an event in the event list with the given id.\n' \
                   '`!setEventName` - sets the name of an event in the event list with the given id.\n' \
                   '`!clearEvents` - clears all the events in the current event list.\n' \
                   '`!removeEvent` - removes the event with the given id from the event list.'
        await self.get_destination().send(response)

    async def send_command_help(self, command):
        return self.get_destination().send(command.description)
