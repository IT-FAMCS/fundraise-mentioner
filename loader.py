import logging
from pyrogram import Client
from pathlib import Path
from decouple import config


DIR = Path(__file__).absolute().parent


#variables are defined in .env
API_TOKEN = config("API_TOKEN")
API_ID = config("API_ID")
API_HASH = config("API_HASH")

logging.basicConfig(
    level=logging.WARN,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{DIR}/logs.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)
app = Client("bot", api_hash=API_HASH, api_id=API_ID, bot_token=API_TOKEN)

