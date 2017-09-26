import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="test", pm_help=None)

@client.event
async def on_ready():
    print("Bot Online!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run("token")
