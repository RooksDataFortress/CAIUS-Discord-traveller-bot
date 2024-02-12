import csv
from csv import reader
with open("sectordata.tsv", "r", encoding="utf8") as sector_file:
    tsv_reader = csv.DictReader(sector_file, delimiter="\t")
    for system in tsv_reader:
        hex = system["Hex"]
        bases = (system["Bases"])
        remarks = system["Remarks"]
        name = system["Name"]
        zone = system["Zone"]
        print(f'{hex} = ("{name}", "{zone}", "{bases}", "{remarks}")')
#        print(f"{name} is zone {zone}")





#data = []
#with open('sectordata.tsv', newline='') as f:
#    for row in reader(f, delimiter='\t'):
#        data.append(row)
#    
#    for row in data:
#        print(row)

#with open("sectordata.tsv", "r", encoding="utf8") as sec_file:
#    tsv_reader = csv.reader(sec_file, delimiter="\t")
#
#    # Skip the first row, which is the header
#   next(tsv_reader)
#
#   for row in tsv_reader:
#       (Sector, SS, Hex, Name, UWP, Bases, Remarks, Zone, PBG, Allegiance, Stars, Ix, Ex, Cx, Nobility, W, RU) = row
#       print(f"{Name} is zone {Zone}")