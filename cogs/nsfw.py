import discord
import hmtai
import random
from discord.ext import commands

class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hentai(self, ctx):
        cat = ['hentai', 'bdsm', 'uniform', 'cum', 'femdom', 'tentacles', 'nsfwNeko', 'ero', 'yuri']
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v2', random.choice(cat)))

def setup(bot):
    bot.add_cog(Nsfw(bot))
