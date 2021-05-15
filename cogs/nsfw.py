import discord
import hmtai
from discord.ext import commands

class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM('v1', 'hentai'))
        else:
            await ctx.send('Не тут.')

def setup(bot):
    bot.add_cog(Nsfw(bot))
