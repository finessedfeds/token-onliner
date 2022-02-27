import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

import keep_alive

keep_alive.keep_alive()

#TOKEN
TOKEN = os.getenv("TOKEN")

client = discord.Client()
b = Bot(command_prefix = "ayy")

@b.event
async def on_ready():
    print("ayy lmao")

b.run(TOKEN, bot = False)

