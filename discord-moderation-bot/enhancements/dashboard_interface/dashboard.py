import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def warn(ctx, member: discord.Member, reason: str):
    await ctx.send(f'{member.mention} has been warned for: {reason}')

@bot.command()
async def mute(ctx, member: discord.Member, duration: int, reason: str):
    await ctx.send(f'{member.mention} has been muted for {duration} minutes for: {reason}')

@bot.command()
async def kick(ctx, member: discord.Member, reason: str):
    await ctx.send(f'{member.mention} has been kicked for: {reason}')

@bot.command()
async def ban(ctx, member: discord.Member, reason: str):
    await ctx.send(f'{member.mention} has been banned for: {reason}')

@bot.command()
async def vote_kick(ctx, member: discord.Member):
    await ctx.send(f'Vote initiated to kick {member.mention}')

@bot.command()
async def reputation(ctx, member: discord.Member):
    await ctx.send(f'{member.mention} has a positive reputation in the server')

@bot.command()
async def assign_role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'{member.mention} has been assigned the role: {role.name}')

@bot.command()
async def appeal(ctx, action: str, reason: str):
    await ctx.send(f'Your appeal for {action} has been submitted with reason: {reason}')

bot.run('YOUR_TOKEN')