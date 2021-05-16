import discord
import hmtai
from discord.ext import commands

class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v2', 'hentai'))
        else:
            await ctx.send('Не тут.')

    @commands.command()
    async def bdsm(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v2', 'bdsm'))
        else:
            await ctx.send('Не тут.')

    @commands.command()
    async def gif(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v2', 'gif'))
        else:
            await ctx.send('Не тут.')

    @commands.command()
    async def uniform(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v2', 'uniform'))
        else:
            await ctx.send('Не тут.')

    @commands.command()
    async def cum(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v2', 'cum'))
        else:
            await ctx.send('Не тут.')

def setup(bot):
    bot.add_cog(Nsfw(bot))
