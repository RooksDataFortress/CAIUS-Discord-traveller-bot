import requests
from sectordata import *

import csv
from csv import reader
with open("sectordata.tsv", "r", encoding="utf8") as sector_file:
    tsv_reader = csv.DictReader(sector_file, delimiter="\t")
    for system in tsv_reader:
        name = system["Name"]
        hex = system["Hex"]
#        worldapisearch = requests.get(f'https://travellermap.com/api/search?q={name} in:spin')
#        worlddata = worldapisearch.json()
#        items = worlddata.get("Results", {}).get("Items", [])
#        hexx = items[0].get("World", {}).get("HexX")
#        hexy = items[0].get("World", {}).get("HexY")
        print("Generating map for coords", hex)
        jumpmapimg = (f'https://travellermap.com/api/jumpmap?sector=spin&hex={hex}&jump=4&scale=120&.png')
        mapimage = requests.get(jumpmapimg).content 
        print("creating map file for", name)
        f = open(f'{name}.png','wb')
        f.write(mapimage) 
        f.close() 