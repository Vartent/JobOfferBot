from telegram_bot.app import dp
from aiogram import executor
import telegram_bot.handlers

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
