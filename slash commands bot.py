import nextcord
from nextcord.ext import commands
from nextcord import Interaction

Intents = nextcord.Intents.default()

Intents.message_content = True

Intents.members = True

bot = commands.Bot(command_prefix="!", intents=Intents)

@bot.event

async def on_ready():

    print(f"Logged in as {bot.user}")

@bot.slash_command(name="me", description="info about you :)", guild_ids=[1316669327830810675])

async def me(interaction: Interaction,     member: nextcord.Member):


    embed = nextcord.Embed(title='', color=nextcord.Color.blue())

    embed.add_field(name="Requsted by: ", value=member.name, inline=True)

    embed.set_footer(icon_url=member.avatar)


    embed.add_field(name='Member Name', value=member.mention, inline=False)

    embed.add_field(name="Member Id", value=member.id, inline=False)

    embed.add_field(name="Member Status", value=member.status, inline=False)

    embed.add_field(name="Member Activites", value=member.activities, inline=False)

    embed.set_image(url=member.avatar)

    embed.add_field(name="Requsted by: ", value=member.name, inline=True)

    embed.set_footer(icon_url=member.avatar)

    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="user", description="show your when you join at server when you creat your account", guild_ids=[1316669327830810675])

async def user(interaction: Interaction, member: nextcord.Member):

    embed = nextcord.Embed(title="", color=nextcord.Color.purple())


    embed.add_field(name="Requsted by: ", value=member.name, inline=True)

    embed.set_footer(icon_url=member.avatar)

    embed.add_field(name="joined server: ", value=member.joined_at, inline=True)

    embed.add_field(name="creat account: ", value=member.created_at, inline=True)

    embed.set_thumbnail(url=member.avatar)


    embed.add_field(name="Requsted by: ", value=member.name, inline=True)

    embed.set_footer(icon_url=member.avatar)

    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="avatar", description="show your avatar", guild_ids=[1316669327830810675])

async def avatar(interaction: Interaction, member: nextcord.Member):

    embed = nextcord.Embed(title="", color=nextcord.Color.dark_gold())

    
    embed.add_field(name="Requsted by: ", value=member.name, inline=True)
    
    embed.set_footer(icon_url=member.avatar)

    embed.set_image(url=member.avatar)

    
    embed.add_field(name="Requsted by: ", value=member.name, inline=True)
    
    embed.set_footer(icon_url=member.avatar)

    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="delete", description="Delete messages", guild_ids=[1316669327830810675])

async def delete(interaction: Interaction, amont: int):

    await interaction.response.defer()

    await interaction.channel.purge(limit=amont)

    await interaction.followup.send("i done")

    
@bot.slash_command(name="ban", description="ban bad users", guild_ids=[1316669327830810675])

async def ban(interaction: Interaction, member: nextcord.Member, reasons: str):

    await interaction.response.defer()

    await member.ban(reason=reasons)

    await interaction.followup.send(f"{member.mention} has been banned for: {reasons}")
