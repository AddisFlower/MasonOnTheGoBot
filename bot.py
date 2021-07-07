import os
from os import listdir
import discord
from discord.ext import commands
from dotenv import load_dotenv

from help import MasonHelpCommand

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', help_command=MasonHelpCommand())

if __name__ == '__main__':
    """Loads the cogs from the './cogs' folder."""

    for cog in listdir('./cogs'):
        if cog.endswith('.py'):
            bot.load_extension(f'cogs.{cog[:-3]}')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your instructions :)'))
    print(f'{bot.user} has connected to Discord!')


bot.run(TOKEN)
