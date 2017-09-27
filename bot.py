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

@client.command()
async def serverinfo(ctx):
    em = discord.Embed(title='**Server Info**', colour=0xDEAFBF)
    em.add_field(name="Human Count", value="%s humans" %sum(not member.bot for member in ctx.guild.members), inline=True)
    em.add_field(name="Bot Count", value="%s bots" %sum(member.bot for member in ctx.guild.members), inline=True)
    await ctx.send(embed=em)

@client.command()
async def debug(ctx):
    print(sum(not member.bot for member in ctx.guild.members))

client.run("token")
