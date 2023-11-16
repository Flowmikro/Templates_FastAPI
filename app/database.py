from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb://localhost:27017/app/mongodb"
client = AsyncIOMotorClient(MONGODB_URL)
db = client['mongodb']
collection = db['templates']
