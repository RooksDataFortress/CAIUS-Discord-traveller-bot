import pymongo
client = pymongo.MongoClient()
db = client["wanderer-configs"]

collection = db.training

#Define the data to be inserted or updated
data = {
    "character": "",
    "train_skill": "Deception 0",
    "Check leg": "5",
    "discordname": "toxika_edm",
}

#Update the document with the same config_name or insert if it doesn't exist
collection.update_one(
    {"character": "Echo"},  # Filter criteria
    {"$set": data},  # New values
    upsert=True  # If document does not exist, insert it
)
print("Data inserted or updated successfully.")

# Find a document with a specific character
document = collection.find_one({"character": "Church"})

# Check if the document exists and retrieve parameter1
if document:
    charname = document.get("character")
    skill = document.get("train_skill")
    player = document.get("discordname")
    check = document.get("Check leg")
    print("Value :", charname, skill, player, check)
else:
    print("Document with those details not found.")

#print all train checks
x = collection.find()
for document in x:
    print(x)