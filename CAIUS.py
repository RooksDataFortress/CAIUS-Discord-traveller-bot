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
import wget

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
    worldembed_colour = 0x055FFF

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

@client.tree.command()
@app_commands.describe(worldname='Desired world name to search in the database.')
async def jumpmap(interaction: discord.Interaction, worldname: str):
    jumpembed_title = f"Jump 4 map for: {worldname}"
    jumpembed_colour = 0x055FFF 

    worldapisearch = requests.get(f"https://travellermap.com/api/search?q={worldname}")
    worlddata = worldapisearch.json()
    items = worlddata.get("Results", {}).get("Items", [])
    hexx = items[0].get("World", {}).get("HexX")
    hexy = items[0].get("World", {}).get("HexY")
    coords = (f'{hexx}{hexy}')
    jumpmapimg = (f'https://travellermap.com/api/jumpmap?sector=spin&hex={coords}&jump=4&scale=120&.png')
    jumpembed = discord.Embed(color=jumpembed_colour, title=jumpembed_title, description=f'')   
    jumpembed.add_field(name="Map data" , value=jumpmapimg, inline=False)
    await interaction.response.send_message(embed=jumpembed)

@client.tree.command()
async def freerooms(interaction: discord.Interaction):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command
        rooms_title = "Passenger positions available!"
        rooms_colour = 0x055FFF
        roomsembed = discord.Embed(color=rooms_colour, title=rooms_title, description=f'I have crunched the numbers and we have the following room vacancies for the upcoming leg of the journey.')
        availhigh = (random.randint(2,12))
        roomsembed.add_field(name="High rooms available:" , value=availhigh, inline=False)
        availstan = (random.randint(2,200))
        roomsembed.add_field(name="Standard rooms available:" , value=availstan, inline=False)
        availbasic = (random.randint(3,300))
        roomsembed.add_field(name="Basic passage available:" , value=availbasic, inline=False)
        availlow = (random.randint(2,100))
        roomsembed.add_field(name="Low berths available:" , value=availlow, inline=False)
        await interaction.response.send_message(embed=roomsembed)
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

client.run(token)