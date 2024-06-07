import discord

class CloseButton(discord.ui.Button):
    def __init__(self, ticket_id):
        super().__init__(style=discord.ButtonStyle.red, label="Close Ticket")
        self.ticket_id = ticket_id

    async def callback(self, interaction: discord.Interaction):
        ticket_channel = discord.utils.get(interaction.guild.channels, name=f"ticket-{self.ticket_id}")
        if ticket_channel:
            await ticket_channel.delete()
        else:
            await interaction.response.send_message("Ticket channel not found.", ephemeral=True)