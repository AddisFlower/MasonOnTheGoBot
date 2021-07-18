from discord.ext import commands
import discord
from datetime import time


class ChannelSetup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setNotificationChannel', description="Sets the channel where the notifications and traffic updates are sent.")
    async def set_channel(self, ctx, *, channel_name):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        channel_id = channel.id
        self.bot.channel_id = channel_id
        await self.reload_extensions()
        response = "Notifications and traffic updates will be sent in the " + channel_name + " channel now!"
        await ctx.send(response)

    @commands.command(name='setNotificationTime', description='Sets the time the two notifications are sent (Time must be sent in military time).')
    async def set_time(self, ctx, hour, minutes):
        self.bot.WHEN = time(int(hour), int(minutes), 0)
        await self.reload_extensions()
        await ctx.send("Time has been successfully changed!")

    async def reload_extensions(self):
        self.bot.unload_extension(f'cogs.Traffic')
        self.bot.unload_extension(f'cogs.Covid')
        self.bot.unload_extension(f'cogs.Weather')
        self.bot.load_extension(f'cogs.Traffic')
        self.bot.load_extension(f'cogs.Covid')
        self.bot.load_extension(f'cogs.Weather')


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(ChannelSetup(bot))
