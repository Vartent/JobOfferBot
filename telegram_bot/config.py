import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ERD_API_KEY = os.environ.get("ERD_API_KEY")
OW_API_KEY = os.environ.get("OW_API_KEY")
