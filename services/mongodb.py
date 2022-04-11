import asyncio
import motor.motor_asyncio
from pymongo import MongoClient
from services.log import log

# ExBtjomtE7O1FLmj
# sync_client = MongoClient("mongodb+srv://root:ExBtjomtE7O1FLmj@serverlessinstance0.ngtgq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
async_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://JavaBoy:Anirban@cluster0.2sfbj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000)
#motor.motor_asyncio.AsyncIOMotorClient

try:
    db = async_client['main']
    log.info("MONGO DB STARTED")
except Exception as e:
    log.warn(e)