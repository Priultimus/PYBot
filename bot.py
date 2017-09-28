import discord
from discord.ext import commands
import logging
import json
import datetime

logger = logging.getLogger('discord')
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="test", pm_help=None)

def ms_chop(time):
    timesp = str(time).split('.', 1)
    return timesp[0]

@client.event
async def on_ready():
    print("Bot Online!")
    await client.change_presence(game=discord.Game(name='I Exist!'))

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def serverinfo(ctx):
    em = discord.Embed(title='**Server Info**', colour=0xDEAFBF)
    em.add_field(name="Human Count", value="%s humans" %sum(not member.bot for member in ctx.guild.members), inline=True)
    em.add_field(name="Bot Count", value="%s bots" %sum(member.bot for member in ctx.guild.members), inline=True)
    em.add_field(name="Server Creation Date", value="%s" %ms_chop(ctx.guild.created_at), inline=True)
    em.add_field(name="Server Owner", value="%s" %ctx.guild.owner, inline=True)
    await ctx.send(embed=em)

@client.command()
async def debug(ctx):
    print("Debug Message Goes Here")

json_data = json.load(open("config.json"))
client.run(json_data['token'])
