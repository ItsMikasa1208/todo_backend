from typing import Optional
from pymongo import AsyncMongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from core.config import settings

class Database:
    client : AsyncMongoClient = None
    database : Optional[Database] = None

    user : Collection
    token : Collection
    notes : Collection
    priority : Collection
    status : Collection

db = Database()

async def connect_db():
    try:
        if not settings.MONGODB_URI:
            raise("MongoDB URI isn't defined!!!")
        
        db.client = AsyncMongoClient(settings.MONGODB_URI)
        db.database = db.client.get_database("notes")
        
        #Collections
        db.user = db.database["user"]
        db.token = db.database["token"]
        db.notes = db.database["notes"]
        db.priority = db.database["priority"]
        db.status = db.database["status"]


    except Exception as e:
        print(e)
