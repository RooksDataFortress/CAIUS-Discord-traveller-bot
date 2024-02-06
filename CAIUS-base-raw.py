#! python
import time
import sys
import random
sys.stdout.write("Good evening shoppers, its time for the night market! Get your eddies ready because this stock wont last! \n")
categories = ["Food and drugs", "Personal Electronics", "Weapons and Armor", "Cyberware", "Clothing and Fashionware", "Survival Gear"]
foods = ["Canned Goods (10eb)", "Packaged goods (10eb)", "Frozen Goods (10eb)", "Bags of Grain (20eb)", "Kibble Pack (10eb)", "Bags of Prepak (20eb)", "Street Drugs up 20eb", "Poor Quality Alcohol (10eb)", "Alcohol (20eb)", "Excellent Quality Alcohol (100)", "MRE (10eb)", "Live Chicken (50eb)", "Live Fish (50eb)", "Fresh Fruits (50eb)", "Fresh Vegetables (50eb)", "Root Vegetables (20eb)", "Live Pigs (100eb)", "Exotic Fruits (100eb)", "Exotic Vegetables (100eb)", "Street Drugs of Exactly 50eb" ]
electronics= ["Agent (100eb)", "Programs and hardware of (100eb)or less", "Audio Recorder (100eb)", "Bug Detector (500eb)", "Chemical Analyzer (1,000eb)", "Computer (50eb) ", "Cyberdeck (500eb) ", "Cyberdeck (500eb) ", "Disposable Cell Phone (50eb) ", "Electric Guitar or Other Instrument (500eb) ", "Programs or Hardware of exactly (500eb)", "Medscanner (1,000eb)", "Homing Tracer (500eb) ", "Radio Communicator (100eb) ", "Techscanner (1,000eb)", "Smart Glasses (500eb)", "Radar Detector (500eb) ", "Scrambler/Descrambler (500eb) ", "Radio Scanner/Music Player (50eb) ", "Braindance Viewer (1,000eb)", "Virtuality Goggles (100eb)"]
combatgear = ["Medium Pistol (50eb) ", "Heavy Pistol or Very Heavy Pistol (100eb)", "SMG (100eb)", "Heavy SMG (100eb)", "Shotgun (500eb)", "Assault Rifle (500eb)", "Sniper Rifle (500eb)", "Bows or Crossbow (100eb)", "Grenade Launcher or Rocket Launcher (500eb)", "Ammunition of (500eb)or less", "A Single Exotic Weapon of GM’s choice", "Light Melee Weapon (50eb) ", "Medium Melee Weapon (50eb) ", "Heavy Melee Weapon (100eb)", "Very Heavy Melee Weapon (100eb)", "Armor of (100eb)or less", "Armor of exactly (500eb)", "Armor of exactly (1,000eb)", "Weapon Attachments of (100eb)or less", "Weapon Attachments of (500eb)or higher"]
cyberware = ["Cybereye (100eb)", "Cyberaudio Suite (500eb)", "Neural Link (500eb)", "Cyberarm (500eb)", "Cyberleg (100eb)", "External Cyberware of exactly (1,000eb)", "External Cyberware of (500eb)or less", "Internal Cyberware of exactly (1,000eb)", "Internal Cyberware of (500eb)or less", "Cybereye Option of exactly (1,000eb)", "Cybereye Option of (500eb)or less", "Cyberaudio Option of exactly (1,000eb)", "Cyberaudio Option of (500eb)or less", "Neuralware Option of exactly (1,000eb)", "Neuralware Option of (500eb)or less", "Cyberlimb Option of exactly (1,000eb)", "Cyberlimb Option of (500eb)or less", "Fashionware of GM’s Choice", "Borgware of GM’s Choice", "Any Cyberware of GM’s Choice"]
clothing = ["Bag Lady Chic", "Gang Colors", "Generic Chic", "Bohemian", "Leisurewear ", "Nomad Leathers", "Asia Pop", "Urban Flash", "Businesswear", "High Fashion", "Biomonitor (100eb)", "Chemskin (100eb)", "EMP Threading (10eb)", "Light Tattoo (100eb)", "Shift Tacts (100eb)", "Skinwatch (100eb)", "Techhair (100eb)", "Generic Chic", "Leisurewear", "Gang Colors"]
survival= ["Anti-Smog Breathing Mask (20eb)", "Auto Level Dampening Ear Protectors (1,000eb)", "Binoculars (50eb) ", "Carryall (20eb)", "Flashlight (20eb)", "Duct Tape (20eb)", "Inflatable Bed & Sleep-bag (20eb)", "Lock Picking Set (20eb)", "Handcuffs (50eb) ", "Medtech Bag (100eb)", "Tent and Camping Equipment (50eb) ", "Rope (60m/yds) (20eb)", "Techtool (100eb)", "Personal CarePak (20eb)", "Radiation Suit (1,000eb)", "Road Flare (10eb)", "Grapple Gun (100eb)", "Tech Bag (500eb)", "Shovel or Axe (50eb) ", "Airhypo (50eb) "]
stocktypes = tuple(random.sample(categories, 2))

currenttime = int(time.time()) 
dealtime = currenttime + 172800
print (dealtime)
print ("<t:",dealtime,">")

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
    count = random.choice([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10])
    inv = tuple(random.sample(goods, count))
    print("\nWe have", count, "offerings of", n,":", "\n > * ", "\n > * ".join(str(x) for x in inv))
#    print ("\n".join(str(el) for el in inv))
    #for x in inv :
        #print (x)  