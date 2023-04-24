from aiogram import Bot, Dispatcher, types
from .config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot=bot, storage=MemoryStorage())
