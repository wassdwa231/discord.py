import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button
from nextcord import Interaction


Intents = nextcord.Intents.default()
Intents.message_content = True
Intents.members = True

bot = commands.Bot(command_prefix="!", intents=Intents)

@bot.event
async def on_ready():
    print("i am ready")

class buttons(View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label="Last vid", style=nextcord.ButtonStyle.blurple)
    async def vid(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("https://youtu.be/rDUmbOzEVFM")

    @nextcord.ui.button(label="channel", style=nextcord.ButtonStyle.blurple)
    async def channel(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("https://www.youtube.com/@AbdullahReviews")

@bot.command()
async def s(ctx):
    view = buttons()
    await ctx.send("Enter", view=view)

class go(View):
    def __init__(self):
        super().__init__(timeout=None)


    @nextcord.ui.button(label="Name", style=nextcord.ButtonStyle.blurple)

    async def name(self,button: Button, interaction: Interaction):

        member = interaction.user

        embed = nextcord.Embed(title="", color=nextcord.Color.red())

        embed.add_field(name="", value=member.name, inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)
        

    @nextcord.ui.button(label="avatar", style=nextcord.ButtonStyle.blurple)
    async def image(self, button: Button, interaction: Interaction):

        member = interaction.user

        embed = nextcord.Embed(title="", color=nextcord.Color.blue())

        embed.set_image(url=member.avatar)

        await interaction.response.send_message(embed=embed, ephemeral=True)


    @nextcord.ui.button(label="Status", style=nextcord.ButtonStyle.blurple)

    async def joined_at_server(self,button: Button, interaction: Interaction):

        member = interaction.user

        embed = nextcord.Embed(title="", color=nextcord.Color.brand_green())

        embed.add_field(name="", value=member.joined_at, inline=False)

    @nextcord.ui.button(label="Id", style=nextcord.ButtonStyle.blurple)

    async def id(self,button: Button, interaction: Interaction):

        member = interaction.user

        embed = nextcord.Embed(title="", color=nextcord.Color.brand_green())

        embed.add_field(name="", value=member.id, inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command()
async def e(ctx):
    view = go()
    await ctx.send("What do you want to know", view=view)

bot.run("TOKEN")
