import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def appeal(ctx):
    # Logic for handling appeal process
    await ctx.send('Please provide details for your appeal.')

bot.run('YOUR_BOT_TOKEN')