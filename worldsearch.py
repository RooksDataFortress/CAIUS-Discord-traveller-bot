import requests
import json
from uwpdata import *
#starports = {'A':"The starport is best in class, it can dock the Wanderer and should accomodate refueling and repairs of any kind.", 'B':"The starport isn't quite big enough to fit the Wanderer, but could offer decent fuel and services.", 'C':"The starport only offers unrefined fuel and it may be in short supply, they can run builds and repairs of crafts under 100 Tons.", 'D':"Barely qualifies as a starport, limited unrefined fuel and nothing in the way of maintenance, shipbuilding or repair facilities.", 'E':"For our purposes, there may as well not be a Starport.", 'X':"No known starport of any kind in the system"}
#sizes = {'0':"The system is some kind of orbital facility or asteroid field. (CAUTION: low gravity world) (Approx less than 5 minutes form orbit to safe jump point.) ", '1':"Approximately 1600KM in diameter. (CAUTION: low gravity world) (Approx 8 Minutes from orbit to safe jump point.)", '2':"3,200KM in diameter. (CAUTION: low gravity world) (Aprox 16 Minutes from orbit to safe jump point.)", '3':"4,800KM in Diameter. (CAUTION: low gravity world) (Approx 23 minutes form orbit to safe jump point.)", '4':"6,400KM in diameter. (CAUTION: low gravity world) (Approx 31 minutes from orbit to safe jump point.)", '5':"8000KM in Diameter. (CAUTION: low gravity world) (Approx 38 Minutes from orbit to safe jump point.)", '6':"9,600KM in diameter. (CAUTION: low gravity world) (Approx 46 minutes from orbit to safe jump point.)", '7':"11,200KM in diameter. (Approx 53 Minutes from orbit to safe jump point.)", '8':"12,800KM in diameter. (Approx 61 minutes form orbit to safe jump point.)", '9':"14,400KM in diameter. (Approx 68 minutes from orbit to safe jump point.)", 'A':"16,000KM in diameter. (CAUTION: High gravity world) (Approx 76 minutes from orbit to safe jump point.)" }
#atmos = {'0':"There is no atmosphere, Vacc suit required.", '1':"Very limited atmosphere, Vacc suit required.", '2':"The atmosphere is both very thin and tainted, Respirator and breathing filters required.", '3':"The atmosphere is very thin, a Respirator is required.", '4':"The atmosphere is both thin and tainted, breathing filters are required.", '5':"The atmosphere is thin but perfectly fine to breathe.", '6':"The atmosphere is optimal.", '7':"The air is tainted, breathing filters are required.", '8':"DANGER: The atmosphere is too dense to support human life at all but the highest of altitudes.", '9':"DANGER: The atmosphere is too dense and tainted to support human life at all but the highest of altitudes and with sufficient breath filters.", 'A':"DANGER: The air is not breathable, you will require your own air supply.", 'B':"DANGER: The air is corrosive, a vacc suit is required.", 'C':"DANGER: The air is extremely corrosive, it will eat away at the seals of all but the most advanced vacc suits.", 'D':"DANGER: The air is extremely dense and not cabable of supporting human life.", 'E':"The atmosphere is very low and only breathable really close to the surface.", 'F':"ALERT: The atmosphere is extremely unusual and defies classification."}
#hydro = {'0':"0-5% Water, A desert world.", '1':"6-15% Surface water.", '2':"16-25% Surface water.", '3':"26-35% Surface water.", '4':"36-45% Surface water.", '5':"46-55% Surface water.", '6':"56-65% Surface water.", '7':"66-75% Surface water.", '8':"76-85% Surface water", '9':"86-95% Surface water, only small landmasses.", 'A':"96-100% Water, a water world."}
#pop = {'0':"Totally unpopulated", '1':"Up to 100 sophonts.", '2':"100-1,000 Sophonts", '3':"1,000-9999 Sophonts.", '4':"10,000-99,999 Sophonts", '5':"100,000-99,999 Sophonts", '6':"1-10 Million Sophonts", '7':"10-100 Million Sophonts.", '8':"100 Million to 1 Billion Sophonts", '9':"1-10 Billion Sophonts.", 'A':"10-100 Billion Sophonts.", 'B':"100 Billion to 1 Trillion Sophonts.", 'C':"More than a Trillion Sophonts."}
#gov = {'0':"There is no organized government of any kind.", '1':"The world is rulled by a Corporate elite", '2':"There is a democratic government in which all citizens have a voice.", '3':"The system is an Oligarchy", '4':"There is a Democratic government of elected representitives.", '5':"The system is ruled by an upper class with powerful technology.", '6':"The government is decided by and answers to a higher power.", '7':"No central government exists, rivals compete for control.", '8':"The system is run by appointed experts.", '9':"Agencies run the system without any input fro regular citizens.", 'A':"A single leader rules the system, he is almost universaly adored by the populace.", 'B':"A single leader rules the system after taking over power, they are not liked as much as their predecessor was.", 'C':"The system is run by Oligarchs who are fairly competent.", 'D':"The system is a religious dictatorship.", 'E':"The world is ruled by a messiah, a single religious leader.", 'F':"A small and all powerful group run a dictatorship in the system."}
#law = {'0':"There is no form of Law and order in the system.", '1':"Law level 1: Battledress, poison gasses and explosives are illegal.", '2':"Law level 2: Combat armor, battledress, explosives, energy and laser weapons are illegal", '3':"Law level 3: Military weapons, and all armor except cloth and mesh are illegal.", '4':"Law level 4: Military, energy and submachine gun weapons are illegal, all armor except Mesh is banned.", '5':"Law level 5: Personal concealable weapons are illegal, Most armors are also illegal.", '6':"Law level 6: All visible armor is banned, All firearms except shotguns and stunners are banned and carrying of any weapons is discouraged.", '7':"Law level 7: All firearms except shotguns and any visible armor is banned.", '8':"Law level 8: all visible weapons and armor are banned.", '9':"Law level 9: Extremely strict with all weapons and armor banned."}
#tech = {'0':"Tech level 0: No technlogy.", '1':"Tech level 1: Primative tools.", '2':"Tech level 2: Renaissance level of technology.", '3':"Tech level 3: Steam power and primative firearms.", '4':"Tech level 4: Industrial technology such as Plastic and Radio.", '5':"Tech level 5: Industrial technology such as basic computing.", '6':"Tech level 6: Industrial technlogy such as primative rockets that can acheive orbit.", '7':"Tech level 7: Pre-stellar technology with space sattelites and widespread computers.", '8':"Tech level 8: Pre-stellar technology that could reach other worlds within their system.", '9':"Tech level 9: Technology ability to create their own jump drives and leave their system.", 'A':"Tech level 10: Technology such as Orbital habitats and factories.", 'B':"Tech level 11: Early stellar technology including artificial intelligences and grav supported superscrapers.", 'C':"Tech level 12: Average stellar technology such as controlling the weather and fusion guns.", 'D':"Tech level 13: Average stellar technology capable of cloning body parts and battledress power armor.", 'E':"Tech level 14: Technlogy such as floating cities and man portable fusion weapons.", 'F':"Tech level 16: The highest rated technology in the known universe, capable of extreme feats such as stopping human aging with anagathic drugs."}
print("Worldsearch test")
secdata = requests.get("https://travellermap.com/api/sec?sector=Spinward Marches")
secdatare = requests.get("https://travellermap.com/api/metadata?sector=Spinward%20Marches")
worldtest = requests.get("https://travellermap.com/api/search?q=Djinni")
#print(secdata.json())
#print(secdatare.json())
worlddata = worldtest.json()
items = worlddata.get("Results", {}).get("Items", [])
uwp_value = items[0].get("World", {}).get("Uwp")
#print(worldtest.json())
print(uwp_value)
print(f"The starport is rated ", uwp_value[0])
print(f"The planet size is ", uwp_value[1])
print(f"The atmoshpere is ", uwp_value[2])
print(f"The hydrographics are ", uwp_value[3])
print(f"The population is ", uwp_value[4])
print(f"The government is ", uwp_value[5])
print(f"The law level is ", uwp_value[6])
print(f"The tech level is ", uwp_value[8])
starport = (starports.get(uwp_value[0]))
size = (sizes.get(uwp_value[1]))
air = (atmos.get(uwp_value[2]))
water = (hydro.get(uwp_value[3]))
population = (pop.get(uwp_value[4]))
government = (gov.get(uwp_value[5]))
laws = (law.get(uwp_value[6]))
tl = (tech.get(uwp_value[8]))
print (starport)
print (size)
print (air)
print (water)
print (population)
print (laws)
print (tl)