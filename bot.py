import os
from os import listdir
import discord
from discord.ext import commands
from dotenv import load_dotenv

from help import MasonHelpCommand

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
channel_id = 0
bot = commands.Bot(command_prefix='!', help_command=MasonHelpCommand())

if __name__ == '__main__':
    """Loads the cogs from the './cogs' folder."""

    for cog in listdir('./cogs'):
        if cog.endswith('.py'):
            bot.load_extension(f'cogs.{cog[:-3]}')


@bot.event
async def on_ready():
    """Instructions for whenever the bot is running"""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your instructions :)'))
    print(f'{bot.user} has connected to Discord!')

    # set the default notification channel as the general channel
    channel = discord.utils.get(bot.get_all_channels(), name="general")
    await bot.get_channel(channel.id).send("Type !help to learn about what I do!")


@bot.event
async def on_command_error(ctx, error):
    """Tells the user to give an existing command whenever he/she tries to invoke a command that does not exist."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Please use a command that is listed under the !help command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the required arguments when using this command.")


@bot.command(name='setNotificationChannel', description="Sets the channel where the notifications and traffic updates are sent.")
async def set_channel(ctx, *, channel_name):
    global channel_id
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    channel_id = channel.id
    await bot.get_channel(channel_id).send("Notifications and traffic updates will be sent in this channel now!")
    print(channel_id)

bot.run(DISCORD_TOKEN)
