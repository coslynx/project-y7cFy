import discord

class ClaimButton(discord.ui.Button):
    def __init__(self, user_id, **kwargs):
        super().__init__(style=discord.ButtonStyle.green, label="Claim")
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Ticket claimed by <@{self.user_id}>", ephemeral=True)

        # Logic to assign the ticket to the specific user with user_id

        await self.view.update_ticket_claimed()