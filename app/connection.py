import pymongo

mongo_uri = "mongodb+srv://YehudaFreiman:3UJrKTTbwPWjuI60@cluster0.gmuqvbk.mongodb.net/"

if not mongo_uri:
    raise RuntimeError("mongo uri not found")

client = pymongo.MongoClient(mongo_uri)
db = client.get_database("test")
collection = db["employee"]
