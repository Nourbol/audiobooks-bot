import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.callback_data import show_callback
from keyboards.inline.choice_buttons import choice
from loader import dp
from utils.apirequests import get_products

product_kb_cb: CallbackData = CallbackData("product_kb_cb", "title")


def generate_menu_keyboard():
    kb = InlineKeyboardMarkup()
    products = get_products()
    for key, product in enumerate(products):
        if product["title"] is None or product["title"] == '':
            continue
        if key % 2 == 0:
            kb.add(InlineKeyboardButton(product["title"], callback_data=product_kb_cb.new(product["title"])))
        else:
            kb.insert(InlineKeyboardButton(product["title"], callback_data=product_kb_cb.new(product["title"])))
    return kb


@dp.message_handler(Text(equals="Menu"))
async def show_menu(message: Message):
    await message.answer(text="Here is our menu.",
                         reply_markup=generate_menu_keyboard())


@dp.callback_query_handler(text_contains="Potato")
async def showing_potato(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer("Name of the product: Potato. \n"
                              "Price: 200KZT")


@dp.callback_query_handler(text_contains="Bread")
async def showing_potato(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer("Name of the product: Bread. \n"
                              "Price: 50KZT")


@dp.callback_query_handler(text_contains="Salt")
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
