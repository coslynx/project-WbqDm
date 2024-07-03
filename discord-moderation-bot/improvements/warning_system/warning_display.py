import discord

class WarningDisplay:
    def __init__(self, client):
        self.client = client

    async def display_warning(self, user, num_warnings):
        embed = discord.Embed(
            title=f"User {user} has received {num_warnings} warnings",
            description="Please be cautious of their behavior",
            color=discord.Color.red()
        )
        await self.client.send(embed=embed)