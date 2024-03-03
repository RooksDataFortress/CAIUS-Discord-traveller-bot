import pymongo
client = pymongo.MongoClient()
db = client["wanderer-configs"]

collection = db.training

# Print the value of the "Check leg" field for each document
print('Current leg to check')
currentleg = input()
documents = collection.find()
for document in documents:
    leg = document.get("Check leg")
    user = document.get("discordname")
    skill = document.get("train_skill")
    if leg == currentleg:
        print("Hello", "@"+user, "Its time to roll your training check for ", skill)
    else:  
        print("Sorry its not your time yet", user)