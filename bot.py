import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='.')


#Events

@bot.event
async def on_ready():
    print('Bot is ready.')

#Commands

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

#Cogs

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('bot token here')
