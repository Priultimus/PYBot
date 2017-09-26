import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot Online!")

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'pong')

client.run("MzYyMzYwNDk1NDI2MTA5NDQx.DKxjoA.CujltVwU0Sl1ejXaYEB2ljOlRKA")
