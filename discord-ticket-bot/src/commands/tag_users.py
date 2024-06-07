import discord

async def tag_users(ctx, user_id: int, message: str):
    try:
        user = await ctx.guild.fetch_member(user_id)
        await user.send(message)
        await ctx.send(f"Message sent to {user.display_name} successfully.")
    except discord.errors.HTTPException:
        await ctx.send("Failed to send message. Please check the user ID and try again.")
    except discord.errors.Forbidden:
        await ctx.send("Unable to send message to this user due to privacy settings.")
    except discord.errors.NotFound:
        await ctx.send("User not found. Please provide a valid user ID.")
    except discord.errors.DiscordException:
        await ctx.send("An error occurred while sending the message. Please try again later.")