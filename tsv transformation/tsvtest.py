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