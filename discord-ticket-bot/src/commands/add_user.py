import discord

async def add_user(ctx, ticket_id, user_id):
    ticket = find_ticket(ticket_id)
    
    if not ticket:
        await ctx.send("Ticket not found.")
        return
    
    if ctx.author.id != ticket["owner_id"]:
        await ctx.send("You do not have permission to add users to this ticket.")
        return
    
    user = ctx.guild.get_member(user_id)
    if not user:
        await ctx.send("User not found.")
        return
    
    if user_id in ticket["users"]:
        await ctx.send("User is already added to the ticket.")
        return
    
    ticket["users"].append(user_id)
    await ctx.send(f"{user.mention} has been added to the ticket.")

    save_ticket(ticket)