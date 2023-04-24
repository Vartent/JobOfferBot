from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, CallbackQuery

from . import handler_constants
from ..services import get_weather_by_location, get_weather_by_city
from ..app import dp,bot
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserCity(StatesGroup):
    city = State()


@dp.callback_query_handler(text=handler_constants.GET_WEATHER_COMMAND)
async def start(call: CallbackQuery):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(text="Send location", request_location=True))
    await UserCity.city.set()
    if call.message.chat.type == 'private':
        await call.message.answer(text='First, I need to know where you are.\n'
                                       'Type in the city name or send me location',
                                  reply_markup=keyboard)
    else:
        await call.message.answer(text='Type in the city name')


@dp.message_handler(state=UserCity.city, content_types=['location'])
async def send_weather(message: Message, state: FSMContext):
    await message.answer(get_weather_by_location(message.location.latitude, message.location.longitude))
    await state.finish()


@dp.message_handler(state=UserCity.city, content_types=['text'])
async def send_city_weather(message: Message, state: FSMContext):
    await message.answer(get_weather_by_city(message.text))
    await state.finish()
