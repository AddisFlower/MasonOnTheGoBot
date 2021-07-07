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
                   '`!currentEvents` - returns the current events happening in GMU\n'
        await self.get_destination().send(response)

    async def send_command_help(self, command):
        return self.get_destination().send(command.description)
