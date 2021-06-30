import discord
import json
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta, time


class MasonHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        return await self.get_destination().send("“Mason On The Go” is the go to discord bot for any GMU student. This bot gives you the most accurate weather alerts for the Northern Virginia area. It also keeps you updated on the latest covid immunization rates in Virginia. This will help you know when Virginia will finally exit the pandemic. “Mason On The Go” is the only bot that keeps you up to date on 511 traffic to help you make smarter choices on what routes to take when you are going to campus or when you are travelling around Fairfax. Additionally, this bot will make sure that you don’t miss out on any important daily events happening at GMU. You will want to use this discord bot over other apps because it caters specifically to you, a GMU student.")

    async def send_command_help(self, command):
        return self.get_destination().send(command.description);
