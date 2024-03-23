import pymongo
client = pymongo.MongoClient()
db = client["wanderer-configs"]

legcollection = db.wandererconfigs
traincollection = db.training

# Print the value of the "Check leg" field for each document
print('Checking leg from DB')
# Find the entry in the collection
document = legcollection.find_one({"config_name": "Currentleg"})
currentleg = document.get("Currentleg")
print("Current leg from the DB is", currentleg)
documents = traincollection.find()
for document in documents:
    leg = document.get("Check leg")
    user = document.get("discordname")
    skill = document.get("train_skill")
    if leg == currentleg:
        print("Hello", "@"+user, "Its time to roll your training check for ", skill)
    else:  
        print("Sorry its not your time yet", user)