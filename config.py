import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "3899724"))
    API_HASH = os.environ.get("API_HASH", "78884de73e8aec575ecbe9cf4e11bf20")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5497473553:AAEwr1m7gEHV7rQPKIo0MrUm-OUvJ3eDsVg") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "486198312")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
