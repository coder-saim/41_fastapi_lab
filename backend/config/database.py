from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = 'mongodb://localhost:27017'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. Successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.farm_app
user_collectoin = db['users']









