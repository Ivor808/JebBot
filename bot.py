import os

import discord
import asyncio

TOKEN = os.environ.get('jeb')

bot = discord.Client()

@bot.event
async def on_message(message):
    # do something with message
    print(message.content)

    if message.content == 'jeb?':
        await message.channel.send('hello!')

bot.run(TOKEN)