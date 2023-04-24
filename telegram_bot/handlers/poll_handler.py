from aiogram import Bot, types
from aiogram.dispatcher import FSMContext

from . import handler_constants
from ..app import dp, bot
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup


class Polls(StatesGroup):
    options = State()
    question = State()
    chat_id = State()


@dp.callback_query_handler(text=handler_constants.CREATE_POLL_COMMAND)
async def ask_question(call: CallbackQuery):
    await Polls.question.set()
    await call.message.answer(text="Please enter your poll question:")


@dp.message_handler(state=Polls.question, content_types=['text'])
async def ask_init_currency(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    await Polls.options.set()
    await bot.send_message(chat_id=message.chat.id, text="Please enter options, separated with comma")


@dp.message_handler(state=Polls.options, content_types=['text'])
async def create_poll(message: Message, state: FSMContext):
    await state.update_data(options=message.text.split(","))
    poll_state = await state.get_data()
    await bot.send_message(chat_id=message.chat.id, text="There you go")
    await bot.send_poll(
        question=poll_state.get('question'),
        options=poll_state.get('options'),
        chat_id=message.chat.id
    )



