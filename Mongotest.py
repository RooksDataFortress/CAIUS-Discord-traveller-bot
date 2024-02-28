import pymongo
client = pymongo.MongoClient()
db = client["wanderer-configs"]
#db2 = client.local

collection = db.wandererconfigs

# Define the data to be inserted or updated
#data = {
#    "config_name": "Currentleg",
#    "Currentleg": "1",
#}

# Update the document with the same config_name or insert if it doesn't exist
#collection.update_one(
#    {"config_name": "Currentleg"},  # Filter criteria
#    {"$set": data},  # New values
#    upsert=True  # If document does not exist, insert it
#)
#print("Data inserted or updated successfully.")

# Find a document with a specific config_name
document = collection.find_one({"config_name": "Currentleg"})

# Check if the document exists and retrieve parameter1
if document:
    legvalue = document.get("Currentleg")
    print("Value :", legvalue)
else:
    print("Document with config_name 'example_config' not found.")

cursor = collection.find()
for document in cursor:
    print(document)