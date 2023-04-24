from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, CallbackQuery

from . import handler_constants
from ..services import get_weather_by_location, get_weather_by_city
from ..app import dp
from aiogram.dispatcher.filters.state import State, StatesGroup


# declare state for storing city data
class UserCity(StatesGroup):
    city = State()


# init the weather providing process
@dp.callback_query_handler(text=handler_constants.GET_WEATHER_CALLBACK)
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


# in case if user is using mobile devise and can provide location for more accurate data response
@dp.message_handler(state=UserCity.city, content_types=['location'])
async def send_weather(message: Message, state: FSMContext):
    await message.answer(get_weather_by_location(message.location.latitude, message.location.longitude))
    await state.finish()


# in case if user cannot provide current location, just type in city name
@dp.message_handler(state=UserCity.city, content_types=['text'])
async def send_city_weather(message: Message, state: FSMContext):
    await message.answer(get_weather_by_city(message.text))
    await state.finish()

