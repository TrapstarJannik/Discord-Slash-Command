# discord Imports
import discord
from discord.ext import commands

# other imports
from typing import Literal, Optional
import datetime

# "bot" for commands/events, prefix ".", permissions "all"
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())

# start message 
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}") # <-- bot name
    print(f"Bot ID: {bot.user.id}") # <-- bot ID
    print("Bot is ready.") # <-- ready message

# command for syncing slash commands
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Guild], spec: Optional[Literal["guild", "global", "clear"]] = None) -> None: # <-- command usages
    embed = discord.Embed(title="Synced successfully!", color=0x99e699)  # <-- embed title and color

    if not guilds:
        if spec == "guild": # <-- sync to the current guild
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "global": # <-- sync to all guilds
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "clear": # <-- clear and sync in the current guild
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else: # <-- sync all slash commands 
            synced = await ctx.bot.tree.sync()

        embed.description = f"Synced `{len(synced)}` slash-command/s {'globally' if spec is None else 'in the current guild.'}" # <-- message about the sync
    
    else:
        ret = 0
        for guild in guilds: # <-- for guild ID's 
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException: # <-- sync with discord 
                pass
            else:
                ret += 1

        embed.description = f"Synced to `{ret}/{len(guilds)}` Guild/s." # <-- Message about sync for multiple guilds

    if ctx.author.avatar:
        avatar_url = ctx.author.avatar.url # <-- getting avatar 
    else:
        avatar_url = ctx.author.default_avatar.url # <-- getting default avatar if avatar is none
    embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%H:%M:%S')}", icon_url=avatar_url)  # <-- embed footer (you can change %H:%M:%S to your time format)

    await ctx.send(embed=embed) # <-- send embed


# ping command
    
@bot.tree.command(name="ping", description="Shows the bot's ping")
async def ping(interaction: discord.Interaction):
    requester_name = interaction.user.name # <-- getting username
    requester_avatar_url = interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url # <-- getting avatar 
    latency = round(bot.latency * 1000) # <-- convert to milliseconds
    current_time = datetime.datetime.now().strftime("%H:%M:%S") # <-- time (you can change %H:%M:%S to your time format)
    ping_embed = discord.Embed(title="🏓 Pong!...", description=f"My ping is `{latency}ms`.", color=0xccccff) 
    ping_embed.set_footer(text=f"{requester_name}・{current_time}", icon_url=requester_avatar_url) # <-- embed footer 
    await interaction.response.send_message(embed=ping_embed) # <-- send embed 
    
# add more code here
#>


# end - run bot  
with open("token.txt") as f: # <-- token = token.txt (security to upload the code safely)
    token = f.read()

bot.run(token)
