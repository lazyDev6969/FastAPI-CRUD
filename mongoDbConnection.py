from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("")

db = client["product_db"]
collection = db["products"]

