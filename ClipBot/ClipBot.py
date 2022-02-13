from lib2to3.pgen2 import token
import os, asyncio
import discord
from dotenv import load_dotenv
import random
from subprocess import run
from CaptionInserter import caption
from ClipExtractor import extract

from discord.ext import commands, tasks
from discord.ext.commands import bot
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command(name='clip')
async def send_clip(ctx, arg=None):
    clips = os.listdir('out/')
    if len(clips) < 1:
        await ctx.send('You need to extract the newest clips with the !update command.')
    if arg in ["1", "2", "3","4","5"]:
        rand = int(arg)-1
    else:
        rand = random.randint(0, len(clips)-1)
    await ctx.send('Enjoy your clip!', file=discord.File('out/' + clips[rand]))

@bot.command(name='update')
async def extract_clips(ctx):
    await ctx.send("Extracting the hottest clips! This might take a while, so why don't you grab a cup of coffee and I'll let you know when it's done?;)")
    extract()
    caption()
    try:
        await ctx.send("Extracting complete! Check out the hottest clips with !clip.", file=discord.File('finally.jpg'))
    except:
        await ctx.send("Extracting complete! Check out the hottest clips with !clip.")


@tasks.loop(minutes=180)
async def auto_update():
    channel = client.get_channel('942077346410823770')
    channel.send("Auto update started! Getting the newest clips, so please wait 5 minutes before using the !clip command.")
    channel.send("Update finished! Enjoy the new hottest clips!")
    try:
        extract()
        caption()
        try:
            channel.send("Update finished! Enjoy the new hottest clips!", file=discord.File('finally.jpg'))
        except:
            channel.send("Update finished! Enjoy the new hottest clips!")
    except:
        channel.send("hey! something went wrong...please run !update manually!")


@bot.command(name='info')
async def info(ctx):
    await ctx.send("Hi! I am the clipbot made by Team42 for the GUTS2022 Hackathon AssemblyAI challenge!\nYou can try me out by typing !clip, or !update if there are no clips available. Have fun!")

@auto_update.before_loop
async def my_background_task_before_loop():
    await client.wait_until_ready()

auto_update.start()

bot.run(TOKEN)