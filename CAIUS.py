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
from tradecalc import *
import pymongo

#Configure the database
client = pymongo.MongoClient()
db = client["wanderer-configs"]

#Configure the discord token
token = os.getenv("token")
new_line = '\n'
MY_GUILD = discord.Object(id=1191987404853215262)  # replace with your guild id

#conifigure the discord commands and sync them locally
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
    worldfile = (worldname + ".png")
    file = discord.File(f'D:\DEV-local\CAIUS-Discord-traveller-bot\maps\{worldfile}', filename='map.png')
    embed = discord.Embed()
    embed.set_image(url="attachment://image.png")
    await interaction.response.send_message(file=file)

@client.tree.command()
@app_commands.describe(leg='Which leg of the journey we are on')
async def db_legset(interaction: discord.Interaction, leg: str):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command

        #Set db to wandererconfig
        collection = db.wandererconfigs
        #Define the data to be inserted or updated
        data = {
            "config_name": "Currentleg",
            "Currentleg": leg,
        }

        #Update the document with the same config_name or insert if it doesn't exist
        collection.update_one(
            {"config_name": "Currentleg"},  # Filter criteria
            {"$set": data},  # New values
            upsert=True  # If document does not exist, insert it
        )

        # Find a document with a specific config_name
        document = collection.find_one({"config_name": "Currentleg"})
        # Check if the document exists and retrieve parameter1
        if document:
            legvalue = document.get("Currentleg")
            print("Data inserted or updated successfully. New value is", legvalue)
        else:
            print("Document with config_name 'example_config' not found.")

        #configure embed
        embed_title = f'Database Update'
        embed_colour = 0x055FFF
        embed = discord.Embed(color=embed_colour, title=embed_title, description="")
        embed.add_field(name=(f'Current journey stop no:'), inline=True , value=legvalue)
        await interaction.response.send_message(embed=embed)
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

#below are the commands related to training
@client.tree.command()
@app_commands.describe(char='Characters first name')
@app_commands.describe(skill='skill name and value')
@app_commands.describe(player='players discord username')
@app_commands.describe(check='Which leg of the journey they roll their check')
async def train_register(interaction: discord.Interaction, char: str, skill: str, player: str, check: str):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command

        #Set db to training db
        collection = db.training
        #Define the data to be inserted or updated
        data = {
            "character": char,
            "train_skill": skill,
            "Check leg": check,
            "discordname": player,
        }

        #Update the document with the same config_name or insert if it doesn't exist
        collection.update_one(
            {"character": char},  # Filter criteria
            {"$set": data},  # New values
            upsert=True  # If document does not exist, insert it
        )

        # Find a document with a specific config_name
        document = collection.find_one({"character": char})
        # Check if the document exists and retrieve parameter1
        if document:
            charname = document.get("character")
            skill = document.get("train_skill")
            player = document.get("discordname")
            check = document.get("Check leg")
            print("details added:", charname, skill, player, check)
        else:
            print("Database error.")

        #configure embed
        embed_title = f'Database Update'
        embed_colour = 0x055FFF
        embed = discord.Embed(color=embed_colour, title=embed_title, description="")
        embed.add_field(name=(f'Training details registered for'), inline=True , value=char)
        await interaction.response.send_message(embed=embed)
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

@client.tree.command()
async def train_check(interaction: discord.Interaction):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command

        #Set db endpoints
        legcollection = db.wandererconfigs
        traincollection = db.training

        #Check the current leg
        document = legcollection.find_one({"config_name": "Currentleg"})
        currentleg = int(document.get("Currentleg"))
        print("Current leg from the DB is", currentleg)

        trainstats = ""
        documents = traincollection.find()
        for document in documents:
            leg = int(document.get("Check leg"))
            user = document.get("discordname")
            skill = document.get("train_skill")
            char = document.get("character")
            if leg <= currentleg:
                trainstats = (trainstats + f'Congrats {char}, Its time to roll your training check for: {skill}{new_line}')
            else:  
                trainstats = (trainstats + f'Sorry its not your time yet {char}{new_line}')
        #configure embed
        embed_title = f'Staff Training status'
        embed_colour = 0x055FFF
        embed = discord.Embed(color=embed_colour, title=embed_title, description="")
        embed.add_field(name=(f'Current Leg as per our database is {currentleg}'), inline=False , value=f'if incorrect, please alert administration.')
        embed.add_field(name=(f'Staff Training status:'), inline=False , value=trainstats) 
        embed.add_field(name=(f'Is your name missing?'), inline=False , value=f"Please register for the training program.")         
        await interaction.response.send_message(embed=embed)
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

#The investment management and event commands
@client.tree.command()
@app_commands.describe(risk='Enter risk profile (low, significant, high, extreme, ridiculous)')
@app_commands.describe(val='What is the value of the investment')
@app_commands.describe(bonus='What is the total DM of the stat and skill used to manage the fund')
async def invest(interaction: discord.Interaction, risk: str, val: str, bonus: str):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
    
        #Outline the different risk profiles.
        risk_profiles = {
            'low': {'DC': 4, 'effect_percentage': 0.75},
            'significant': {'DC': 6, 'effect_percentage': 1.5},
            'high': {'DC': 8, 'effect_percentage': 2},
            'extreme': {'DC': 10, 'effect_percentage': 3},
            'ridiculous': {'DC': 12, 'effect_percentage': 5}
        }

        #risk profile function
        def get_risk_profile(profile_name):        
            #Get the DC and effect percentage for a given risk profile name
            #Args: profile_name (str): The name of the risk profile.
            #Returns: tuple: A tuple containing the DC and effect percentage.
            profile = risk_profiles.get(profile_name.lower())
            if profile is not None:
                return profile['DC'], profile['effect_percentage']
            else:
                raise ValueError("Invalid risk profile name. Choose from 'low', 'significant', 'high', 'extreme', 'ridiculous'.")

        profile_name = risk
        initial_value = float(val)
        dm_bonus = int(bonus)
        initial_value_rounded = round(initial_value)

        DC, effect_percentage = get_risk_profile(profile_name)

        event_die = random.randint(1, 36)

        if event_die == 36:
            event_status = (f"There is an event!")
            eventflag = "yes"
        else:
            event_status = (f"No event this time.")
            eventflag = "no"

        manager_roll = random.randint(1, 6) + random.randint(1, 6)
        effect = manager_roll + dm_bonus - DC

        if effect <= -6:
            effectmessage = "Disastrous failure! Significant loss incurred."
        elif -5 < effect <= -4:
            effectmessage =  "Major setback! Considerable loss incurred."
        elif -3 < effect <= -1:
            effectmessage =  "Minor setback. Small loss incurred."
        elif 0 == effect:
            effectmessage =  "No significant change. Investment is stable."
        elif 0 <= effect <= 5:
            effectmessage =  "Moderate success! Noticeable gain."
        elif  effect >= 6:
            effectmessage =  "Outstanding success! Significant gain."
        else:
            effectmessage = "Syntax error"
    
        # Calculate the impact on the investment value
        investment_effect = initial_value * (effect_percentage / 100) * effect
        final_investment_value = initial_value + investment_effect

        # Round the final investment value to the nearest whole number
        final_investment_value_rounded = round(final_investment_value)

        embed_title = "Investment Management"
        embed_colour = 0x055FFF
        embed = discord.Embed(color=embed_colour, title=embed_title, description=f'Investment management report')
        embed.add_field(name=f'Current value' , value=f"{initial_value_rounded}Cr", inline=False)
        embed.add_field(name=f'Portfolio risk' , value=risk, inline=True)        
        embed.add_field(name=f'Management DM' , value=dm_bonus, inline=True)  
        embed.add_field(name=f'Result' , value=effectmessage, inline=False)
        embed.add_field(name=f'New value' , value=f"{final_investment_value_rounded}Cr", inline=False)
        embed.add_field(name=f'Investment event status' , value=event_status, inline=False)   

        #event handle
        if eventflag == "yes":
            die1 = random.randint(1,6)
            die2 = (random.randint(1,6)+random.randint(1,6))
            events = {
                2: ["📉 Catastrophe! 📉", f'Natural disaster wipes {die2*10}% from the value of an estate or property. If this reduces it to zero the holding is utterly destroyed.'],
                3: ["📉 Market Crash! 📉", f'All the businesses, pensions, stipends and stocks in a portfolio lose {die1*10}% of their value.'],
                4: ["📉 Military Posturing 📉", f'An impending war threatens the material basis of one of a portfolios financial assets, which loses {die1*10}% from its value.'],
                5: ["📉 Insider trading 📉", "Accusations of improper procedures causes the loss of a months income from one financial asset in the portfolio."],
                6: ["📉 Markets Fall 📉", f'All portfolio income lowered by 10% for a month.'],
                7: ["Markets stable", "Nothing occurs."],
                8: ["📈 Markets rise 📈", f'All portfolio income raised by 10% for a month.'],
                9: ["📈 Bonus Dividends 📈", f'A bumper payout doubles the monthly income of one financial asset in the portfolio.'],
                10: ["📈 Tax Restructuring 📈", f'The revision of a law category allows one of a portfolios financial assets, to gain {die1*10}% to its value.'],
                11: ["📈 Market Boom! 📈", f'All the businessses, pensions, stipends and stocks in a portfolio gain {die1*10}% of their value.'],
                12: ["📈 Trendy! 📈", f'The produce of an estate or location of a property suddenly becomes fashionable, raising the value of the holding by {die2*10}%.']
            }
            eventroll = (random.randint(1,6)+random.randint(1,6))
            event = events[eventroll]
            die1 = random.randint(1,6)
            die2 = (random.randint(1,6)+random.randint(1,6))
        
            adjusted_value = final_investment_value_rounded
            if eventroll == 2:
                adjusted_value -= final_investment_value_rounded * (die2 * 0.1)
            elif eventroll in [3, 4]:
                adjusted_value -= final_investment_value_rounded * (die1 * 0.1)
            elif eventroll == 5:
                adjusted_value == initial_value_rounded
            elif eventroll == 6:
                adjusted_value -= (final_investment_value_rounded - initial_value_rounded) / 10  
            elif eventroll == 8:
                adjusted_value += (final_investment_value_rounded - initial_value_rounded) / 10      
            elif eventroll == 9:
                adjusted_value += (final_investment_value_rounded - initial_value_rounded) * 2  
            elif eventroll in [10, 11]:
                adjusted_value += final_investment_value_rounded * (die1 * 0.1)
            elif eventroll == 12:
                adjusted_value += final_investment_value_rounded * (die2 * 0.1)
            
            final_adjusted_value = round(adjusted_value)

            embed.add_field(name=event[0] , value=event[1], inline=False)
            embed.add_field(name="Adjusted value" , value=f"{adjusted_value}Cr", inline=False)

        await interaction.response.send_message(embed=embed)            

    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

#Below are the commands related to passenger rooms and DM's
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

# Below are the commands related to trading.
@client.tree.command()
@app_commands.describe(system='Desired system to trade in.')
async def tradestock(interaction: discord.Interaction, system: str):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command

        #define embed
        embed_title = f'Available trade goods in {system}'
        embed_colour = 0x055FFF
        embed = discord.Embed(color=embed_colour, title=embed_title, description="")
        
        #get system zone and trade coee data
        tradesystem = requests.get(f'https://travellermap.com/api/search?q={system} in:spin')
        tradedata = tradesystem.json()
        items = tradedata.get("Results", {}).get("Items", [])
        hexx = items[0].get("World", {}).get("HexX")
        hexy = items[0].get("World", {}).get("HexY")
        coords = (f'{hexx}{hexy}')
        hcoords = (f'h{coords}')
        hcoordszone = globals()[hcoords]
        remarks = (hcoordszone[3])

        #Add the common goods
        goodsname = ""
        goodsamount = ""
        goodscost = ""
        for x in commongoods:
            goodsname = (goodsname + f'{x[0]}{new_line}')
            goodsamount = (goodsamount + f'{x[1]}{new_line}')
            goodscost = (goodscost + f'{x[2]}{new_line}') 

        
        for x in tradegoods:
            availcodes = x[3].split()
            commoncodes = set(syscodes) & set(availcodes)
            if commoncodes:
                goodsname = (goodsname + f'{x[0]}{new_line}')
                goodsamount = (goodsamount + f'{x[1]}{new_line}')
                goodscost = (goodscost + f'{x[2]}{new_line}') 

        randgoodscount = random.randint(1,6)
        randgoods = tuple(random.sample(allgoods, randgoodscount))
        for x in randgoods:
            goodsname = (goodsname + f'{x[0]}{new_line}')
            goodsamount = (goodsamount + f'{x[1]}{new_line}')
            goodscost = (goodscost + f'{x[2]}{new_line}') 
        embed.add_field(name=(f'Good type'), inline=True , value=goodsname)
        embed.add_field(name=(f'Tons available'), inline=True , value=goodsamount)
        embed.add_field(name=(f'Base Price (Cr)'), inline=True , value=goodscost)
        await interaction.response.send_message(embed=embed)
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")
    
@client.tree.command()
@app_commands.describe(system='Desired system to trade in.')
async def tradedms(interaction: discord.Interaction, system: str):
    #Check if the user has the required role
    required_role_name = "Administrator"
    required_role = discord.utils.get(interaction.guild.roles, name=required_role_name)
    if required_role in interaction.user.roles:
        #User has the required role, proceed with the command

        #define embed
        embed_title = f'Difficulty to trade in {system}'
        embed_colour = 0x055FFF
        embed = discord.Embed(color=embed_colour, title=embed_title, description="")
        
        #get system zone and trade coee data
        tradesystem = requests.get(f'https://travellermap.com/api/search?q={system} in:spin')
        tradedata = tradesystem.json()
        items = tradedata.get("Results", {}).get("Items", [])
        hexx = items[0].get("World", {}).get("HexX")
        hexy = items[0].get("World", {}).get("HexY")
        coords = (f'{hexx}{hexy}')
        hcoords = (f'h{coords}')
        hcoordszone = globals()[hcoords]
        destzone = (hcoordszone[1])
        tradezone = ""
        remarks = (hcoordszone[3])
        if destzone == "A":
            tradezone = "Amber"
            remarks += " za"
            print ("zone is amber")
        elif destzone == "R":
            tradezone = "Red"
            remarks += " zr"
            print ("zone is red")
        else:
            tradezone = "Normal"

        goodsname = ""
        goodsbuydm = ""
        goodsselldm = ""

        for good, mods in zip(commongoods, goodmods):
            total_modifier = 0
        
            #Iterate over each system code for this type of good
            for code in remarks.split():
                if code in mods:
                    total_modifier += mods[code]
            goodsname = (goodsname + f'{good[0]}{new_line}')
            goodsbuydm = (goodsbuydm + f'{total_modifier}{new_line}')     
            goodsselldm = (goodsselldm + f'{(total_modifier*-1)}{new_line}')    
        
        for good, mods in zip(tradegoods, tradegoodsmods):
            total_modifier = 0
        
            #Iterate over each system code for this type of good
            for code in remarks.split():
                if code in mods:
                    total_modifier += mods[code]
            goodsname = (goodsname + f'{good[0]}{new_line}')
            goodsbuydm = (goodsbuydm + f'{total_modifier}{new_line}')     
            goodsselldm = (goodsselldm + f'{(total_modifier*-1)}{new_line}')   

        embed.add_field(name=(f'Good type'), inline=True , value=goodsname)
        embed.add_field(name=(f'Buy DM'), inline=True , value=goodsbuydm)
        embed.add_field(name=(f'Sell DM'), inline=True , value=goodsselldm)
        await interaction.response.send_message(embed=embed)
    else:
        #User does not have the required role, send a message indicating access denied
        await interaction.response.send_message("Error: You lack staff access to use that function.")

client.run(token)