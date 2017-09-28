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

def load_cogs():
    client.load_extension('tests')
    
@client.event
async def on_ready():
    print("Bot Online!")
    load_cogs()
    await client.change_presence(game=discord.Game(name='I Exist!'))


json_data = json.load(open("config.json"))
client.run(json_data['token'])
