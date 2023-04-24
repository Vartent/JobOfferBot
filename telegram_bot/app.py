from aiogram import Bot, Dispatcher, types
from .config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6143113557:AAFTd17dyKhsgPw75LmnUEYY7M2G-o9ZnwE")

dp = Dispatcher(bot=bot, storage=MemoryStorage())
