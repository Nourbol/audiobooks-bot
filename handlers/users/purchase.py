import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_data import buy_callback
from keyboards.inline.choice_buttons import choice
from loader import dp


@dp.message_handler(Text(equals="Menu"))
async def show_menu(message: Message):
    await message.answer(text="Here is our menu. \n"
                         "If you want to go back — press \"cancel\" button",
                         reply_markup=choice)



@dp.callback_query_handler(text_contains="Potato")
async def showing_potato(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer("Name of the product: Vladisgay. \n"
                              "Price: Priceless")

@dp.callback_query_handler(text_contains="Bread")
async def showing_potato(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer("Name of the product: Bread. \n"
                              "Price: 50KZT")

@dp.callback_query_handler(text_contains="Potato")
async def showing_potato(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer("Name of the product: Salt. \n"
                              "Price: 200KZT")

@dp.callback_query_handler(text="cancel")
async def cancel_showing(call: CallbackQuery):
    await call.answer("Питонистов держат в подвале, спасите", show_alert=True)
    await call.message.edit_reply_markup()
