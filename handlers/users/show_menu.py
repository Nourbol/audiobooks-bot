import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.callback_data import show_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, bot
from utils.apirequests import get_products, get_product, get_orders
from states.order_products import orders


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

    kb.add(InlineKeyboardButton("Cancel", callback_data="cancel"))
    return kb


@dp.message_handler(Text(equals="Menu"))
async def show_menu(message: Message):
    await message.answer(text="Here is our menu.",
                         reply_markup=generate_menu_keyboard())


products_show_kb_cb: CallbackData = CallbackData("products_show_kb_cb", "title")

ordering = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Order this product", callback_data="order")
    ],
    [
        InlineKeyboardButton(text="Cancel ordering", callback_data="cancel")
    ]
]
)


@dp.callback_query_handler(product_kb_cb.filter())
async def cb_products_show_id(call: CallbackQuery, callback_data: dict):
    title = callback_data["title"]
    product = get_product(title)
    text = f"Title: {product['title']}\n" \
           f"Details: {product['details']}\n" \
           f"Price: {product['price']}\n"
    await bot.send_message(call.message.chat.id, text)
    await call.message.answer(f"Would you like to order this product?", reply_markup=ordering)


@dp.callback_query_handler(text="order")
async def add_order(call: CallbackQuery, callback_data: dict):
    title = callback_data["title"]
    order = get_product(title)
    get_orders(order)
    await call.message.answer(f"Your order list has been succesfully uploaded")

@dp.callback_query_handler(text="cancel")
async def cancel_showing(call: CallbackQuery):
    await call.message.edit_reply_markup()
