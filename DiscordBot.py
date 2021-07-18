import os
from os import listdir
import discord
from datetime import time
from discord.ext import commands
from dotenv import load_dotenv
from Help import MasonHelpCommand

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', help_command=MasonHelpCommand())
bot.WHEN = time(7, 0, 0)  # The two notifications are sent at 7:00 AM
bot.channel_id = 0

if __name__ == '__main__':
    """Loads the cogs from the './cogs' folder."""

    for cog in listdir('./cogs'):
        if cog.endswith('.py'):
            bot.load_extension(f'cogs.{cog[:-3]}')


@bot.event
async def on_ready():
    """Instructions for whenever the bot is running"""
    channel = discord.utils.get(bot.get_all_channels(), name="general")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='your instructions :)'))
    print(f'{bot.user} has connected to Discord!')
    bot.channel_id = channel.id
    await bot.get_channel(bot.channel_id).send("Type !help to learn about what I do!")


@bot.event
async def on_command_error(ctx, error):
    """Tells the user to give an existing command whenever he/she tries to invoke a command that does not exist."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Please use a command that is listed under the !help command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the required arguments when using this command.")


bot.run(TOKEN)
