from typing import Optional
import os
import discord
from discord import app_commands
import sys
import random
import time

#Night market categories
categories = ["Food and drugs", "Personal Electronics", "Weapons and Armor", "Cyberware", "Clothing and Fashionware", "Survival Gear"]
foods = ["Canned Goods (10eb)", "Packaged goods (10eb)", "Frozen Goods (10eb)", "Bags of Grain (20eb)", "Kibble Pack (10eb)", "Bags of Prepak (20eb)", "Street Drugs up 20eb", "Poor Quality Alcohol (10eb)", "Alcohol (20eb)", "Excellent Quality Alcohol (100)", "MRE (10eb)", "Live Chicken (50eb)", "Live Fish (50eb)", "Fresh Fruits (50eb)", "Fresh Vegetables (50eb)", "Root Vegetables (20eb)", "Live Pigs (100eb)", "Exotic Fruits (100eb)", "Exotic Vegetables (100eb)", "Street Drugs of Exactly 50eb" ]
electronics= ["Agent (100eb)", "Programs and hardware of (100eb)or less", "Audio Recorder (100eb)", "Bug Detector (500eb)", "Chemical Analyzer (1,000eb)", "Computer (50eb) ", "Cyberdeck (500eb) ", "Cyberdeck (500eb) ", "Disposable Cell Phone (50eb) ", "Electric Guitar or Other Instrument (500eb) ", "Programs or Hardware of exactly (500eb)", "Medscanner (1,000eb)", "Homing Tracer (500eb) ", "Radio Communicator (100eb) ", "Techscanner (1,000eb)", "Smart Glasses (500eb)", "Radar Detector (500eb) ", "Scrambler/Descrambler (500eb) ", "Radio Scanner/Music Player (50eb) ", "Braindance Viewer (1,000eb)", "Virtuality Goggles (100eb)"]
combatgear = ["Medium Pistol (50eb) ", "Heavy Pistol or Very Heavy Pistol (100eb)", "SMG (100eb)", "Heavy SMG (100eb)", "Shotgun (500eb)", "Assault Rifle (500eb)", "Sniper Rifle (500eb)", "Bows or Crossbow (100eb)", "Grenade Launcher or Rocket Launcher (500eb)", "Ammunition of (500eb)or less", "A Single Exotic Weapon of GM’s choice", "Light Melee Weapon (50eb) ", "Medium Melee Weapon (50eb) ", "Heavy Melee Weapon (100eb)", "Very Heavy Melee Weapon (100eb)", "Armor of (100eb)or less", "Armor of exactly (500eb)", "Armor of exactly (1,000eb)", "Weapon Attachments of (100eb)or less", "Weapon Attachments of (500eb)or higher"]
cyberware = ["Cybereye (100eb)", "Cyberaudio Suite (500eb)", "Neural Link (500eb)", "Cyberarm (500eb)", "Cyberleg (100eb)", "External Cyberware of exactly (1,000eb)", "External Cyberware of (500eb)or less", "Internal Cyberware of exactly (1,000eb)", "Internal Cyberware of (500eb)or less", "Cybereye Option of exactly (1,000eb)", "Cybereye Option of (500eb)or less", "Cyberaudio Option of exactly (1,000eb)", "Cyberaudio Option of (500eb)or less", "Neuralware Option of exactly (1,000eb)", "Neuralware Option of (500eb)or less", "Cyberlimb Option of exactly (1,000eb)", "Cyberlimb Option of (500eb)or less", "Fashionware of GM’s Choice", "Borgware of GM’s Choice", "Any Cyberware of GM’s Choice"]
clothing = ["Bag Lady Chic", "Gang Colors", "Generic Chic", "Bohemian", "Leisurewear ", "Nomad Leathers", "Asia Pop", "Urban Flash", "Businesswear", "High Fashion", "Biomonitor (100eb)", "Chemskin (100eb)", "EMP Threading (10eb)", "Light Tattoo (100eb)", "Shift Tacts (100eb)", "Skinwatch (100eb)", "Techhair (100eb)", "Generic Chic", "Leisurewear", "Gang Colors"]
survival= ["Anti-Smog Breathing Mask (20eb)", "Auto Level Dampening Ear Protectors (1,000eb)", "Binoculars (50eb) ", "Carryall (20eb)", "Flashlight (20eb)", "Duct Tape (20eb)", "Inflatable Bed & Sleep-bag (20eb)", "Lock Picking Set (20eb)", "Handcuffs (50eb) ", "Medtech Bag (100eb)", "Tent and Camping Equipment (50eb) ", "Rope (60m/yds) (20eb)", "Techtool (100eb)", "Personal CarePak (20eb)", "Radiation Suit (1,000eb)", "Road Flare (10eb)", "Grapple Gun (100eb)", "Tech Bag (500eb)", "Shovel or Axe (50eb) ", "Airhypo (50eb) "]

token = os.getenv("token")
new_line = '\n'
MY_GUILD = discord.Object(id=1191987404853215262)  # replace with your guild id
#THEIR_GUILD = discord.Object(id=611115334971162624) 


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
#        self.tree.copy_global_to(guild=THEIR_GUILD)
#        await self.tree.sync(guild=THEIR_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print('Computer core operational! Shard Identity is is {0.user}'.format(client))
    print('------')

@client.tree.command()
async def nightmarket(interaction: discord.Interaction):
    currenttime = int(time.time()) 
    dealtime = currenttime + 172800
    await interaction.response.send_message(f'> # Good evening shoppers, its time for the night market! {new_line} > **Get your eddies ready because this stock wont last! {new_line} > This offer expires at <t:{dealtime}>**')
    stocktypes = tuple(random.sample(categories, 2))
    for n in stocktypes:
        if n == "Food and drugs":
            goods = foods
        elif n == "Personal Electronics":
            goods = electronics
        elif n == "Weapons and Armor":
            goods = combatgear
        elif n == "Cyberware":
            goods = cyberware
        elif n == "Clothing and Fashionware":
            goods = clothing
        elif n == "Survival Gear":
            goods = survival
        else: print ("error: goods cannot be found, sorry.[this is a bug in the code]")
        print("Good evening shoppers, its time for the night market! Get your eddies ready because this stock wont last!")
        count = random.choice([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10])
        print("We have", count, "offerings of", n,":")
        inv = tuple(random.sample(goods, count))
        """Lists the goods"""
        await interaction.followup.send(f'**> We have {count} offerings of {n}:**{new_line}> * {"\n > * ".join(str(x) for x in inv)}')

# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.

#@client.tree.command()
#@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
#async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
#    """Says when a member joined."""
#    # If no member is explicitly provided then we use the command user here
#    member = member or interaction.user
#
#    # The format_dt function formats the date time into a human readable representation in the official client
#    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


# A Context Menu command is an app command that can be run on a member or on a message by
# accessing a menu within the client, usually via right clicking.
# It always takes an interaction as its first parameter and a Member or Message as its second parameter.

# This context menu command only works on members

#@client.tree.context_menu(name='Show Join Date')
#async def show_join_date(interaction: discord.Interaction, member: discord.Member):
#    # The format_dt function formats the date time into a human readable representation in the official client
#    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')

client.run(token)