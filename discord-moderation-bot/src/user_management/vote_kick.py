import discord

class VoteKick:
    def __init__(self, client):
        self.client = client
        self.votes = {}

    async def start_vote_kick(self, message, user):
        if user.id in self.votes:
            await message.channel.send("There is already a vote kick in progress for this user.")
        else:
            self.votes[user.id] = {"voters": set(), "votes": 0}
            await message.channel.send(f"A vote kick has been initiated for {user.name}. Type !vote yes to kick.")

    async def vote_yes(self, message, user):
        if user.id in self.votes and user.id not in self.votes[user.id]["voters"]:
            self.votes[user.id]["voters"].add(user.id)
            self.votes[user.id]["votes"] += 1
            await message.channel.send(f"{user.name} has voted to kick.")

            if self.votes[user.id]["votes"] >= len(message.guild.members) // 2:
                await message.guild.kick(user, reason="Vote kick passed.")
                del self.votes[user.id]
                await message.channel.send(f"{user.name} has been successfully kicked.")
        elif user.id in self.votes:
            await message.channel.send("You have already voted.")
        else:
            await message.channel.send("There is no vote kick in progress for this user.")

    async def cancel_vote_kick(self, message, user):
        if user.id in self.votes:
            del self.votes[user.id]
            await message.channel.send("Vote kick has been canceled.")
        else:
            await message.channel.send("There is no vote kick in progress for this user.")

    async def handle_vote_kick(self, message):
        if message.content.startswith('!startvote'):
            user_id = message.content.split(' ')[1]
            user = message.guild.get_member(int(user_id))
            await self.start_vote_kick(message, user)
        elif message.content.startswith('!vote yes'):
            await self.vote_yes(message, message.author)
        elif message.content.startswith('!cancelvote'):
            await self.cancel_vote_kick(message, message.author)