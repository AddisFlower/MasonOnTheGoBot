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
        await self.bot.get_channel(channel_id).send("Notifications and traffic updates will be sent in this channel now!")
        print(channel_id)


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(ChannelSetup(bot))
