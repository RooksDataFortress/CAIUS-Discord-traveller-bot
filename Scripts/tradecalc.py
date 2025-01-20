import random
import requests
import json
from .sectordata import *

tradesystem = requests.get("https://travellermap.com/api/search?q=Inthe")

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
print ("system at", {hcoords}, " is zone", tradezone)
print ("Relevant trade codes are:", remarks)

#common goods
cmnelec = ["Common electronics", ((random.randint(1,6)+random.randint(1,6))*10), "20,000", "Ag As Ba De Fl Ga Hi Ht IeIn Lo Lt Na Ni Po Ri Va Wa"]
cmnelecmods = {"Ht":+3, "In":+2, "Ri":+1, "Lo":-1, "Ni":-2, "Po":-1}
cmnig = ["Common industrial goods", ((random.randint(1,6)+random.randint(1,6))*10), "10,000", "Ag As Ba De Fl Ga Hi Ht IeIn Lo Lt Na Ni Po Ri Va Wa"]
cmnigmods = {"In":+5, "Na":+2, "Ag":-2, "Ni":-3}
cmnmg = ["Common manufactured goods", ((random.randint(1,6)+random.randint(1,6))*10), "20,000", "Ag As Ba De Fl Ga Hi Ht IeIn Lo Lt Na Ni Po Ri Va Wa"]
cmnmgmods = {"In":+5, "Na":+2, "Hi":-2, "Ni":-3}
cmnrm = ["Common raw materials", ((random.randint(1,6)+random.randint(1,6))*20), "5,000", "Ag As Ba De Fl Ga Hi Ht IeIn Lo Lt Na Ni Po Ri Va Wa"]
cmnrmmods = {"Ag":+3, "Ga":+2, "In":-2, "Po":-2}
cmncons = ["Common consumables", ((random.randint(1,6)+random.randint(1,6))*20), "500", "Ag As Ba De Fl Ga Hi Ht IeIn Lo Lt Na Ni Po Ri Va Wa"]
cmonconsmods = {"Ag":+3, "As":-4, "Ga":+1, "Wa":+2, "As":-1, "Fl":-1, "Hi":-1, "Le":-1}
cmnore = ["Common ore", ((random.randint(1,6)+random.randint(1,6))*20), "1,000", "Ag As Ba De Fl Ga Hi Ht IeIn Lo Lt Na Ni Po Ri Va Wa"]
cmnoremods = {"As":+4, "In":-3, "Ni":-1}

#trade goods
advelect =["Advanced electronics", (random.randint(1,6)*5), "100,000", "Ht In"]
advelectmods = {"Ht":+3, "In":+2, "As":-3, "Ni":-1, "Ri":-2}
advmp = ["Advanced machine parts", (random.randint(1,6)*5),	"75,000", "Ht In"]
advmpmods = {"Ht":+1, "In":+2, "As":-2, "Ni":-1}
advmg = ["Advanced manufactured goods", (random.randint(1,6)*5), "100,000", "Ht In"]
advmgmods = {"In":+1, "Hi":-1, "Ri":-2}
advwep = ["Advanced weapons", (random.randint(1,6)*5), "150,000", "Ht In"]
advwepmods = {"Ht":+2, "Po":-1, "Za":-2, "Zr":-4}
advveh = ["Advanced vehicles", (random.randint(1,6)*5), "180,000", "Ht In"]
advvehmods = {"Ht":+2, "As":-2, "Ri":-2}
bio = ["Biochemicals", (random.randint(1,6)*5), "50,000", "Ag Wa"]
biomods = {"Ag":+1, "Wa":+2, "In":-2}
crys = ["Crystals and gems", (random.randint(1,6)*5), "20,000", "As De Le"]
crysmods = {"As":+2, "De":+1, "Le":+1, "In":-3, "Ri":-2}
cyber = ["Cybernetics", (random.randint(1,6)), "250,000", "Ht"]
cybermods = {"Ht":+1, "As":-1, "Le":-1, "Ri":-2}
liveani = ["Live animals", (random.randint(1,6)*10),"10,000", "Ag Ga"]
liveanimods = {"Ag":+2, "Lo":-3}
luxcons = ["Luxury consumables", (random.randint(1,6)*10), "20,000", "Ht Ga Wa"]
luxconsmods = {"Ag":+2, "Wa":+1, "Hi":-2, "Ri":-2}
luxgd = ["Luxury goods", (random.randint(1,6)), "200,000", "Hi"]
luxgdmods = {"Hi":+1, "Ri":-1}
med = ["Medical supplies", (random.randint(1,6)*5), "50,000", "Hi Ht"]
medmods = {"Ht":+2, "In":-2, "Po":-1, "Ri":-1}
pchem = ["Petrochemicals", (random.randint(1,6)*10), "10,000", "De Fl IeWa"]
pchemmods = {"De":+2, "Ag":-1, "In":-2, "Lo":-2}
pharma = ["Pharmaceuticals", (random.randint(1,6)), "100,000", "As De Hi Wa"]
pharmamods = {"As":+2, "Hi":+1, "Lo":-1, "Ri":-2}
poly = ["Polymers", (random.randint(1,6)*10), "7,000", "In"]
polymods = {"In":+1, "Ni":-1, "Ri":-2}
precmet = ["Precious metals", (random.randint(1,6)), "50,000", "As De Fl Le"]
precmetmods = {"As":+3, "De":+1, "Ie":+2, "Ht":-1, "In":-2, "Ri":-3}
rad = ["Radioactives", (random.randint(1,6)), "1,000,000", "As De Lo"]
radmods = {"As":+2, "Lo":+2, "Ag":-3, "Ht":-1, "In":-3, "Ni":-2}
robot = ["Robots", (random.randint(1,6)*5), "400,000", "In"]
robotmods = {"In":+1, "Ag":-2, "Ht":-1}
spice = ["Spices", (random.randint(1,6)*10), "6,000", "De Ga Wa"]
spicemods = {"De":+2, "Hi":-2, "Po":-3, "Ri":-3}
text = ["Textiles", (random.randint(1,6)*20), "3,000", "Ag Ni"]
textmods = {"Ag":+7, "Hi":-3, "Na":-2}
uncore = ["Uncommon ore", (random.randint(1,6)*20), "5,000", "As Le"]
uncoremods = {"As":+4, "In":-3, "Ni":-1}
uncrm = ["Uncommon raw materials", (random.randint(1,6)*10), "20,000", "Ag De Wa"]
uncrmmods = {"Ag":+2, "Wa":+1, "Ht":-1, "In":-2}
wood = ["Wood",	(random.randint(1,6)*20), "1,000", "Ag Ga"]
woodmods = {"Ag":+6, "In":-1, "Ri":-2}
vehicles = ["Vehicles", (random.randint(1,6)*10), "15,000", "Hi In"]
vehiclesmods = {"Ht":+1, "In":+2, "Hi":-1, "Ni":-2}
exotic = ["Exotics", "TBD", "TBD", "TBD"]
exoticmods = []

allgoods = [cmnelec, cmnig, cmnmg, cmnrm, cmncons, cmnore, advelect, advmp, advmg, advwep, advveh, bio, crys, cyber, liveani, luxcons, luxgd, med, pchem, pharma, poly, precmet, rad, robot, spice, text, uncore, uncrm, wood, vehicles]
commongoods = [cmnelec, cmnig, cmnmg, cmnrm, cmncons, cmnore]
tradegoods = [advelect, advmp, advmg, advwep, advveh, bio, crys, cyber, liveani, luxcons, luxgd, med, pchem, pharma, poly, precmet, rad, robot, spice, text, uncore, uncrm, wood, vehicles]
tradegoodsmods = [advelectmods, advmpmods, advmgmods, advwepmods, advvehmods, biomods, crysmods, cybermods, liveanimods, luxconsmods, luxgdmods, medmods, pchemmods, pharmamods, polymods, precmetmods, radmods, robotmods, spicemods, textmods, uncoremods, uncrmmods, woodmods, vehiclesmods]
goodmods = [cmnelecmods, cmnigmods, cmnmgmods, cmnrmmods, cmonconsmods, cmnoremods]

mods = 0
syscodes = remarks.split()