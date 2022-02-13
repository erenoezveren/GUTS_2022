from lib2to3.pgen2 import token
import os
import discord
from dotenv import load_dotenv
import random

from discord.ext import commands
from discord.ext.commands import bot
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command(name='clip')
async def send_clip(ctx):
    clips = os.listdir('mp/')
    rand = random.randint(0, len(clips))
    await ctx.send('Enjoy your clip!', file=discord.File('mp/' + clips[rand]))

bot.run(TOKEN)