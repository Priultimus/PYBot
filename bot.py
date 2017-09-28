import discord
from discord.ext import commands
import logging
import json
import datetime

logger = logging.getLogger('discord')
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="test", pm_help=None)

def snowflake_time(id):
    time = datetime.datetime.utcfromtimestamp(((int(id) >> 22) + 1420070400000) / 1000)
    times = "%s" %time
    timesp = times.split('.', 1)
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
    em.add_field(name="Server Creation Date", value="%s" %snowflake_time(ctx.guild.id), inline=False)
    await ctx.send(embed=em)

@client.command()
async def debug(ctx):
    print("Debug Message Goes Here")

json_data = json.load(open("config.json"))
client.run(json_data['token'])
