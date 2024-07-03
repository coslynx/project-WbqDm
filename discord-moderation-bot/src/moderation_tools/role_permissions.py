import discord

class RolePermissions:
    def __init__(self, client):
        self.client = client

    async def has_permission(self, user, required_role):
        member = discord.utils.get(user.guild.roles, name=required_role)
        if member in user.roles:
            return True
        else:
            return False

    async def grant_permission(self, user, role_to_grant):
        role = discord.utils.get(user.guild.roles, name=role_to_grant)
        await user.add_roles(role)

    async def revoke_permission(self, user, role_to_revoke):
        role = discord.utils.get(user.guild.roles, name=role_to_revoke)
        await user.remove_roles(role)