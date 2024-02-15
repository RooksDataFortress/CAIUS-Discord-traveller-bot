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
from sectordata import *

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

    worldapisearch = requests.get(f"https://travellermap.com/api/search?q={worldname} in:spin")
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

    worldapisearch = requests.get(f"https://travellermap.com/api/search?q={worldname} in:spin")
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
async def passengerrooms(interaction: discord.Interaction):
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

#@client.tree.command()
#async def investevent(interaction: discord.Interaction):
#    #Check if the user has the required role
#    required_role_name = "Administrator"
#    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
#    if required_role in interaction.user.roles:
#        #User has the required role, proceed with the command
#        embed_title = ""
#        embed_colour = 0x055FFF
#        embed = discord.Embed(color=embed_colour, title=embed_title, description=f'')
#        availhigh = (random.randint(2,12))
#        embed.add_field(name="" , value=availlow, inline=False)
#        await interaction.response.send_message(embed=embed)
#    else:
#        #User does not have the required role, send a message indicating access denied
#        await interaction.response.send_message("Error: You lack staff access to use that function.")

@client.tree.command()
@app_commands.describe(source_system='System to depart from.')
@app_commands.describe(destination_system='System to travel to.')
async def passengerdms(interaction: discord.Interaction, source_system: str,  destination_system: str):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command
        paxdmembed_title = f"Calculating passenger potential outlook from {source_system} to {destination_system}"
        paxdmembed_colour = 0x055FFF 
        paxdmembed = discord.Embed(color=paxdmembed_colour, title=paxdmembed_title, description=f'__**Contributing factors found:**__')   

        #source world discovery
        srcworldapi = requests.get(f'https://travellermap.com/api/search?q={source_system} in:spin')
        srcdata = srcworldapi.json()
        src_items = srcdata.get("Results", {}).get("Items", [])
        src_uwp_value = src_items[0].get("World", {}).get("Uwp")
        src_hexx = src_items[0].get("World", {}).get("HexX")
        src_hexy = src_items[0].get("World", {}).get("HexY")
        src_coords = (f'{src_hexx}{src_hexy}')
        src_hcoords = (f'h{src_coords}')
        src_hcoordssearch = globals()[src_hcoords]
        #destination world discovery

        destworldapi = requests.get(f'https://travellermap.com/api/search?q={destination_system} in:spin')
        destdata = destworldapi.json()
        dest_items = destdata.get("Results", {}).get("Items", [])
        dest_uwp_value = dest_items[0].get("World", {}).get("Uwp")
        dest_hexx = dest_items[0].get("World", {}).get("HexX")
        dest_hexy = dest_items[0].get("World", {}).get("HexY")
        dest_coords = (f'{dest_hexx}{dest_hexy}')
        dest_hcoords = (f'h{dest_coords}')
        dest_hcoordssearch = globals()[dest_hcoords]

        #Set default DM modifier
        dmmod = 0

        src_zone = (src_hcoordssearch[1])
        src_starport = (src_uwp_value[0])
        src_population = (src_uwp_value[4])
        dest_zone = (dest_hcoordssearch[1])
        dest_starport = (dest_uwp_value[0])
        dest_population = (dest_uwp_value[4])

        srcfac = ""
        destfac = ""

        if src_population in ('0', '1'):
            srcfac = (srcfac + f'- There is barely anyone living in {src_hcoordssearch[0]}, this will be a tricky sell.{new_line}')
            dmmod = (dmmod-4)
        elif src_population in ('6', '7'):
            srcfac = (srcfac + f'- {src_hcoordssearch[0]} is fairly populated, that should help.{new_line}' )
            dmmod = (dmmod+1)
        elif src_population in ('8', '9', 'A', 'B', 'C'):
            srcfac = (srcfac + f'- {src_hcoordssearch[0]} is jam packed! This should be a breeze.{new_line}' )
            dmmod = (dmmod+3)

        if src_starport == 'A':
            srcfac = (srcfac + f'- We are in an amazing starport at {src_hcoordssearch[0]}, there are plenty of oppotunities to sell.{new_line}')
            dmmod = (dmmod+2)
        if src_starport == 'B':
            srcfac = (srcfac + f'- The starport here at {src_hcoordssearch[0]} is pretty good, we can work with this.{new_line}')
            dmmod = (dmmod+1)
        if src_starport == 'E':
            srcfac = (srcfac + f'- The awful starport at {src_hcoordssearch[0]} isn\'t helping our situation..{new_line}')
            dmmod = (dmmod-1)
        if src_starport == 'X':
            srcfac = (srcfac + f'- There isnt even a starport at {src_hcoordssearch[0]}. Where exactly are we meant to be departing from?!{new_line}')
            dmmod = (dmmod-3)

        if src_zone == 'A':
            srcfac = (srcfac + f'- {src_hcoordssearch[0]} is marked as an amber zone, there is a high demand to get out of here{new_line}')
            dmmod = (dmmod+1)
        if src_zone == 'R':
            srcfac = (srcfac + f'- {src_hcoordssearch[0]} is a red zoned system under an interdiction, passengers arent even meant to be here!{new_line}')      
            dmmod = (dmmod-4)
        if srcfac == "":
            srcfac = "- None."
        paxdmembed.add_field(name="Current system factors:" , value=srcfac, inline=False) 

        if dest_population in ('0', '1'):
            destfac = (destfac + f'- There is barely anyone living in {dest_hcoordssearch[0]}, this will be a tricky sell.{new_line}')  
            dmmod = (dmmod-4)
        elif dest_population in ('6', '7'):
            destfac = (destfac + f'- {dest_hcoordssearch[0]} is fairly populated, that should help.{new_line}')        
            dmmod = (dmmod+1)
        elif dest_population in ('8', '9', 'A', 'B', 'C'):
            destfac = (destfac + f'- {dest_hcoordssearch[0]} is jam packed! This should be a breeze.{new_line}')    
            dmmod = (dmmod+3)

        if dest_starport == 'A':
            destfac = (destfac + f'- Amazing facilities in {dest_hcoordssearch[0]}, there are plenty of oppotunities to sell.{new_line}')  
            dmmod = (dmmod+2)
        if dest_starport == 'B':
            destfac = (destfac + f'- The starport over in {dest_hcoordssearch[0]} is pretty good, we can work with this.{new_line}')  
            dmmod = (dmmod+1)
        if dest_starport == 'E':
            destfac = (destfac + f'- The awful starport at {dest_hcoordssearch[0]} isn\'t helping our situation..{new_line}')  
            dmmod = (dmmod-1)
        if dest_starport == 'X':
            destfac = (destfac + f'- There isnt even a starport at {dest_hcoordssearch[0]}. Where exactly are we meant to be dropping them off?!{new_line}')  
            dmmod = (dmmod-3)
        if dest_zone == 'A':
            destfac = (destfac + f'- {dest_hcoordssearch[0]} is marked as an amber zone, there is a higher demand to get there.{new_line}')  
            dmmod = (dmmod+1)
        if dest_zone == 'R':
            destfac = (destfac + f'- {dest_hcoordssearch[0]} is a red zoned system under an interdiction, passengers arent even meant to go there!{new_line}')  
            dmmod = (dmmod-4)
        if destfac == "":
            destfac = "- None."
        paxdmembed.add_field(name="Destination system factors:" , value=destfac, inline=False)         

        paxdmembed.add_field(name=(f'High passenger DM'), inline=True , value=f"> {dmmod-4}")
        paxdmembed.add_field(name=(f'Standard/Basic DM'), inline=True , value=f"> {dmmod}")
        paxdmembed.add_field(name=(f'Low DM'), inline=True , value=f"> {dmmod+1}")
        await interaction.response.send_message(embed=paxdmembed)    
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

client.run(token)