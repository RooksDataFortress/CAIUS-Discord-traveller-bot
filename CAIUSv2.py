from typing import Optional
import os
import discord
from discord import app_commands
import sys
import random
import time
import requests
import json
from uwpdata import *

token = os.getenv("token")
new_line = '\n'
MY_GUILD = discord.Object(id=1191987404853215262)  # replace with your guild id

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)



intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print('Computer core operational! Shard Identity is is {0.user}'.format(client))
    print('------')

@client.tree.command()
@app_commands.describe(worldname='Desired world name to search in the database.')
async def worldsearch(interaction: discord.Interaction, worldname: str):
    worldembed_title = f"Databse entry for {worldname}"
    worldembed_colour = 0xffec00 

    worldapisearch = requests.get(f"https://travellermap.com/api/search?q={worldname}")
    worlddata = worldapisearch.json()
    items = worlddata.get("Results", {}).get("Items", [])
    uwp_value = items[0].get("World", {}).get("Uwp")
    starport = (starports.get(uwp_value[0]))
    size = (sizes.get(uwp_value[1]))
    air = (atmos.get(uwp_value[2]))
    water = (hydro.get(uwp_value[3]))
    population = (pop.get(uwp_value[4]))
    government = (gov.get(uwp_value[5]))
    laws = (law.get(uwp_value[6]))
    tl = (tech.get(uwp_value[8]))

    worldembed = discord.Embed(color=worldembed_colour, title=worldembed_title, description=f'')
    worldembed.add_field(name="UWP" , value=uwp_value, inline=False)
    worldembed.add_field(name="Starport" , value=starport, inline=False)
    worldembed.add_field(name="Size" , value=size, inline=False)
    worldembed.add_field(name="Air" , value=air, inline=False)
    worldembed.add_field(name="Water" , value=water, inline=False)
    worldembed.add_field(name="Population" , value=population, inline=False)
    worldembed.add_field(name="Government" , value=government, inline=False)
    worldembed.add_field(name="Laws" , value=laws, inline=False)
    worldembed.add_field(name="Technology" , value=tl, inline=False)
    await interaction.response.send_message(embed=worldembed)

client.run(token)