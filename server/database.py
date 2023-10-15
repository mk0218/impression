import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

MONGO_HOST = os.getenv("MONGO_HOST",)
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

client = MongoClient(
    "mongodb://"
    f"{MONGO_USERNAME}:"
    f"{MONGO_PASSWORD}@"
    f"{MONGO_HOST}:"
    f"{MONGO_PORT}"
)

db = client.get_database(MONGO_DATABASE)
