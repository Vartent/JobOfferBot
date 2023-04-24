from aiogram.types import CallbackQuery
from ..services import get_cat
from ..app import dp, bot
from . import handler_constants

# Handle the get_cat menu button click
@dp.callback_query_handler(text=handler_constants.GET_CAT_CALLBACK)
async def start(call: CallbackQuery):
    cat_url = await get_cat()
    await call.answer()
    await bot.send_photo(call.message.chat.id, cat_url)
