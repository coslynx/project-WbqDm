import discord

from discord.ext import commands


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn', help='Warn a user for inappropriate behavior')
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                await ctx.send('You cannot warn an admin!')
            else:
                # Logic for warning the user and logging the action
                await ctx.send(f'{member.mention} has been warned for: {reason}')
        else:
            await ctx.send('You do not have permission to warn members.')

def setup(bot):
    bot.add_cog(Warn(bot))