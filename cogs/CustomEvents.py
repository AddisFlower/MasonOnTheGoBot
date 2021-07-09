import os
from discord.ext import commands


class CustomEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addCustomEvent', aliases=['addEvent'],
                      description='Adds a customer event to the event list created by the members of the discord server')
    async def add_custom_event(self, ctx, title, start_date, end_date, description):
        await ctx.send("test")


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(CustomEvents(bot))
