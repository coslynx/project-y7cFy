import discord
from discord.ext import commands

class SetPriority(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_priority')
    async def set_priority(self, ctx, ticket_id: int, priority: str):
        # Logic to set priority for a ticket
        # Make sure to validate input and handle errors gracefully

def setup(bot):
    bot.add_cog(SetPriority(bot))