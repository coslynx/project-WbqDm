import discord

from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.ban_members:
            if member.guild_permissions.ban_members:
                await ctx.send("You cannot ban this user.")
            else:
                await member.ban(reason=reason)
                await ctx.send(f"{member} has been banned.")
        else:
            await ctx.send("You do not have permission to ban members.")

def setup(client):
    client.add_cog(Ban(client))