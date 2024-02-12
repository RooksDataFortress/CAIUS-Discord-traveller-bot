import requests
import json
from uwpdata import *
print("Worldsearch test")
secdata = requests.get("https://travellermap.com/api/sec?sector=Spinward Marches")
secdatare = requests.get("https://travellermap.com/api/metadata?sector=Spinward%20Marches")
worldtest = requests.get("https://travellermap.com/api/search?q=Glisten")
#print(secdata.json())
#print(secdatare.json())
worlddata = worldtest.json()
items = worlddata.get("Results", {}).get("Items", [])
uwp_value = items[0].get("World", {}).get("Uwp")
hexx = items[0].get("World", {}).get("HexX")
hexy = items[0].get("World", {}).get("HexY")
coords = (f'{hexx}{hexy}')
#print(worldtest.json())
#print(uwp_value)
#print(f"The starport is rated ", uwp_value[0])
#print(f"The planet size is ", uwp_value[1])
#print(f"The atmoshpere is ", uwp_value[2])
#print(f"The hydrographics are ", uwp_value[3])
#print(f"The population is ", uwp_value[4])
#print(f"The government is ", uwp_value[5])
#print(f"The law level is ", uwp_value[6])
#print(f"The tech level is ", uwp_value[8])
#starport = (starports.get(uwp_value[0]))
#size = (sizes.get(uwp_value[1]))
#air = (atmos.get(uwp_value[2]))
#water = (hydro.get(uwp_value[3]))
#population = (pop.get(uwp_value[4]))
#government = (gov.get(uwp_value[5]))
#laws = (law.get(uwp_value[6]))
#tl = (tech.get(uwp_value[8]))
#print (starport)
#print (size)
#print (air)
#print (water)
#print (population)
#print (laws)
#print (tl)
print(worlddata)
jumpmapimg = (f'https://travellermap.com/api/jumpmap?sector=spin&hex={coords}&jump=4&scale=120&')
print("Image for jump map is", jumpmapimg)