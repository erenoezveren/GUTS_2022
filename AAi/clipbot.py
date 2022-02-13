from lib2to3.pgen2 import token
import os
import discord
from dotenv import load_dotenv
import random
from subprocess import run
from AssemblyAIproject import caption_clips
from clipextractor import extract_clips

from discord.ext import commands
from discord.ext.commands import bot
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command(name='clip')
async def send_clip(ctx):
    clips = os.listdir('out/')
    if len(clips) < 1:
        await ctx.send('You need to extract the newest clips with the !extract command.')
    rand = random.randint(0, len(clips))
    await ctx.send('Enjoy your clip!', file=discord.File('out/' + clips[rand]))

@bot.command(name='extract')
async def extract_clips(ctx):
    await ctx.send("Extracting the hottest clips! This might take a while, so why don't you grab a cup of coffee?;)")
    extract_clips()
    caption_clips()
    await ctx.send("Extracting complete! Check out the hottest clips with !clip.    ")


bot.run(TOKEN)