# app/database.py
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017")  # Replace with your connection string if needed
db = client["driver_database"]  # Database
drivers_collection = db["drivers"]  # Collection
