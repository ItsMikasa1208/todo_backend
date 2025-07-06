from typing import Optional
from pymongo import AsyncMongoClient
from pymongo.database import Database
from pymongo.collection import Collection


class Database:
    client : AsyncMongoClient = None
    database : Optional[Database] = None

    user : Collection
    token : Collection
    notes : Collection
    priority : Collection
    status : Collection
