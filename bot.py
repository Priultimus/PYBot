import discord
from discord.ext import commands
import logging 

logger = logging.getLogger('discord')
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description=desc, pm_help=None)

@client.event
async def on_ready():
    print("Bot Online!")

@commands.command()
async def ping(self, ctx):
    await ctx.send("Pong")

client.run("Don't include the token when you commit.")
