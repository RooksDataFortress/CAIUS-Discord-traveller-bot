#The Effect of a Broker, Carouse or Streetwise check
#Chief Steward DM+ highest Steward skill on ship
#Rolling for High Passengers DM-4
#Rolling for Low Passengers DM+1
#World Population 1 or less DM-4
#World Population 6-7 DM+1
#World Population 8 or more DM+3
#Starport A DM+2
#Starport B DM+1
#Starport E DM-1
#Starport X DM-3
#Amber Zone DM+1
#Red Zone DM-4
import requests
from sectordata import *
print('Enter Source world:')
src_world = input()
print('Enter Destination world:')
dest_world = input()
#source world discovery
srcworldapi = requests.get(f'https://travellermap.com/api/search?q={src_world} in:spin')
srcdata = srcworldapi.json()
src_items = srcdata.get("Results", {}).get("Items", [])
src_uwp_value = src_items[0].get("World", {}).get("Uwp")
src_hexx = src_items[0].get("World", {}).get("HexX")
src_hexy = src_items[0].get("World", {}).get("HexY")
src_coords = (f'{src_hexx}{src_hexy}')
src_hcoords = (f'h{src_coords}')
src_hcoordssearch = globals()[src_hcoords]
#destination world discovery
destworldapi = requests.get(f'https://travellermap.com/api/search?q={dest_world} in:spin')
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

if src_population in ('0', '1'):
    print (f'There is barely anyone living in {src_hcoordssearch[0]}, this will be a tricky sell.')
    dmmod = (dmmod-4)
    print (f'new dmmod is {dmmod}')
elif src_population in ('6', '7'):
    print (f'{src_hcoordssearch[0]} is fairly populated, that should help.')
    dmmod = (dmmod+1)
    print (f'new dmmod is {dmmod}')
elif src_population in ('8', '9', 'A', 'B', 'C'):
    print (f'{src_hcoordssearch[0]} is jam packed! This should be a breeze.')
    dmmod = (dmmod+3)
    print (f'new dmmod is {dmmod}')

if src_starport == 'A':
    print (f'We are in an amazing starport at {src_hcoordssearch[0]}, there are plenty of oppotunities to sell.')
    dmmod = (dmmod+2)
    print (f'new dmmod is {dmmod}')
if src_starport == 'B':
    print (f'The starport here at {src_hcoordssearch[0]} is pretty good, we can work with this.')
    dmmod = (dmmod+1)
    print (f'new dmmod is {dmmod}')
if src_starport == 'E':
    print (f'The awful starport at {src_hcoordssearch[0]} isn\'t helping our situation..')
    dmmod = (dmmod-1)
    print (f'new dmmod is {dmmod}')
if src_starport == 'X':
    print (f'There isnt even a starport at {src_hcoordssearch[0]}. Where exactly are we meant to be departing from?!')
    dmmod = (dmmod-3)
    print (f'new dmmod is {dmmod}')

if src_zone == 'A':
    print (f'{src_hcoordssearch[0]} is marked as an amber zone, there is a high demand to get out of here.')
    dmmod = (dmmod+1)
    print (f'new dmmod is {dmmod}')
if src_zone == 'R':
    print (f'{src_hcoordssearch[0]} is a red zoned system under an interdiction, passengers arent even meant to be here!')
    dmmod = (dmmod-4)
    print (f'new dmmod is {dmmod}')

if dest_population in ('0', '1'):
    print (f'There is barely anyone living in {dest_hcoordssearch[0]}, this will be a tricky sell.')
    dmmod = (dmmod-4)
    print (f'new dmmod is {dmmod}')
elif dest_population in ('6', '7'):
    print (f'{dest_hcoordssearch[0]} is fairly populated, that should help.')
    dmmod = (dmmod+1)
    print (f'new dmmod is {dmmod}')
elif dest_population in ('8', '9', 'A', 'B', 'C'):
    print (f'{dest_hcoordssearch[0]} is jam packed! This should be a breeze.')
    dmmod = (dmmod+3)
    print (f'new dmmod is {dmmod}')

if dest_starport == 'A':
    print (f'Amazing facilities in {dest_hcoordssearch[0]}, there are plenty of oppotunities to sell.')
    dmmod = (dmmod+2)
    print (f'new dmmod is {dmmod}')
if dest_starport == 'B':
    print (f'The starport over in {dest_hcoordssearch[0]} is pretty good, we can work with this.')
    dmmod = (dmmod+1)
    print (f'new dmmod is {dmmod}')
if dest_starport == 'E':
    print (f'The awful starport at {dest_hcoordssearch[0]} isn\'t helping our situation..')
    dmmod = (dmmod-1)
    print (f'new dmmod is {dmmod}')
if dest_starport == 'X':
    print (f'There isnt even a starport at {dest_hcoordssearch[0]}. Where exactly are we meant to be dropping them off?!')
    dmmod = (dmmod-3)
    print (f'new dmmod is {dmmod}')

if dest_zone == 'A':
    print (f'{dest_hcoordssearch[0]} is marked as an amber zone, there is a higher demand to get there.')
    dmmod = (dmmod+1)
    print (f'new dmmod is {dmmod}')
if dest_zone == 'R':
    print (f'{dest_hcoordssearch[0]} is a red zoned system under an interdiction, passengers arent even meant to go there!')
    dmmod = (dmmod-4)
    print (f'new dmmod is {dmmod}')


print (f'DM for high passengers is {dmmod-4}')
print (f'DM for low passengers is {dmmod+1}')
print (f'DM for standard and basic passengers is {dmmod}')
