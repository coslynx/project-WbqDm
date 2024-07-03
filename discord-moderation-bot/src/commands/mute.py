import discord

from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute')
    async def mute(self, ctx, member: discord.Member, duration: int, *, reason=None):
        # Mute the member for the specified duration with an optional reason
        # Add your mute logic here

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a member to mute.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('Member not found. Please try again.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to mute members.')

def setup(bot):
    bot.add_cog(Mute(bot))