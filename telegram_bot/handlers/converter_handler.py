from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, CallbackQuery, ReplyKeyboardRemove, ChatActions

from . import handler_constants
from ..services import get_currencies, convert_values
from ..app import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup

# declare currencies state
class Currencies(StatesGroup):
    init_curr = State() # currency to convert from
    result_curr = State() # currency to convert to
    amount = State() # amount of money

# return a keyboard with all the currencies available as Coroutine
async def currency_keyboard():
    currencies = await get_currencies()
    buttons = []
    columns = 4
    if type(currencies) == dict:
        buttons: []
        for currency in currencies.keys():
            buttons.append(KeyboardButton(text=currency))

    button_groups = [buttons[i:i + columns] for i in range(0, len(buttons), columns)]
    k = ReplyKeyboardMarkup(resize_keyboard=True)
    for group in button_groups:
        k.row(*group)

    return k

# handle the initiation of currency converting process
@dp.callback_query_handler(text=handler_constants.CONVERT_CURRENCY_CALLBACK)
async def ask_init_currency(call: CallbackQuery):
    await bot.send_chat_action(call.message.chat.id, ChatActions.TYPING)
    keyboard = await currency_keyboard()
    await Currencies.init_curr.set()
    await call.message.answer(text="Select currency that you want to convert\n\nFROM", reply_markup=keyboard)


# got the init currency, ask for result currency
@dp.message_handler(state=Currencies.init_curr, content_types=['text'])
async def ask_init_currency(message: Message, state: FSMContext):
    await state.update_data(init_curr=message.text)
    await Currencies.result_curr.set()
    await message.answer(text="Now select currency that you want to convert\n\nTO")


# got the result currency, ask for amount of money
@dp.message_handler(state=Currencies.result_curr, content_types=['text'])
async def ask_result_currency(message: Message, state: FSMContext):
    await state.update_data(result_curr=message.text)
    await Currencies.amount.set()
    await message.answer(text="No tell me how much?", reply_markup=ReplyKeyboardRemove())

# got the amount, send result
@dp.message_handler(state=Currencies.amount, content_types=['text'])
async def send_result(message: Message, state: FSMContext):
    print(' im in send result')
    await state.update_data(amount=message.text)
    currency_state = await state.get_data()
    await message.answer(text=convert_values(
        currency_state.get('init_curr'),
        currency_state.get('result_curr'),
        currency_state.get('amount')))
    await state.finish()

