import discord

class TranscriptButton(discord.ui.Button):
    def __init__(self, ticket_id):
        super().__init__(style=discord.ButtonStyle.primary, label="Transcript")
        self.ticket_id = ticket_id

    async def callback(self, interaction: discord.Interaction):
        ticket_channel = discord.utils.get(interaction.guild.channels, name=f"ticket-{self.ticket_id}")
        
        if ticket_channel:
            transcript = ""
            async for message in ticket_channel.history(limit=None):
                transcript += f"{message.author.display_name}: {message.content}\n"
            
            await interaction.user.send(f"Transcript for Ticket {self.ticket_id}:\n{transcript}")
        else:
            await interaction.response.send_message("Ticket channel not found.", ephemeral=True)