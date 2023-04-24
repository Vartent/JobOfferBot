from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from ..app import dp
from . import handler_constants


@dp.message_handler(commands=['start'])
async def start(message: Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Get current weather", callback_data=handler_constants.GET_WEATHER_COMMAND))
    keyboard.add(InlineKeyboardButton(text="Convert currency", callback_data=handler_constants.CONVERT_CURRENCY_COMMAND))
    keyboard.add(InlineKeyboardButton(text="Get a cute cat pic", callback_data=handler_constants.GET_CAT_COMMAND))
    keyboard.add(InlineKeyboardButton(text="Create a poll", callback_data=handler_constants.CREATE_POLL_COMMAND))
    await message.answer('Hi there!\nThis bot will help you with many things!\nChoose one', reply_markup=keyboard)

@dp.message_handler(commands=['cancel'], state="*")
async def cancel(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('canceled', reply_markup=ReplyKeyboardRemove())
