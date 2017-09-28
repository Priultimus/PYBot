import discord
from discord.ext import commands
import logging
logger = logging.getLogger('Bot')

class Tests:
    @client.command()
    async def ping(ctx):
        """Ping!"""

        await ctx.send("Pong!")
    @client.command()
    async def serverinfo(ctx):
        """Server info"""
        em = discord.Embed(title='**Server Info**', colour=0xDEAFBF)
        em.add_field(name="Human Count", value="%s humans" %sum(not member.bot for member in ctx.guild.members), inline=True)
        em.add_field(name="Bot Count", value="%s bots" %sum(member.bot for member in ctx.guild.members), inline=True)
        em.add_field(name="Server Creation Date", value="%s" %ms_chop(ctx.guild.created_at), inline=True)
        em.add_field(name="Server Owner", value="%s" %ctx.guild.owner, inline=True)
        await ctx.send(embed=em)

@client.command()
async def debug(ctx):
    logger.info("Message goes here")

def setup(bot):
    bot.add_cog(Tests())
    logger.info("Loaded Tests.")
