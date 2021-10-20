import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.callback_data import show_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, bot
from utils.apirequests import get_products, get_product, add_to_cart
from states.order_products import orders

product_kb_cb: CallbackData = CallbackData("product_kb_cb", "id")


def generate_menu_keyboard():
    kb = InlineKeyboardMarkup()
    products = get_products()
    for key, product in enumerate(products):
        if product["title"] is None or product["title"] == '':
            continue
        if key % 2 == 0:
            kb.add(InlineKeyboardButton(product["title"], callback_data=product_kb_cb.new(id=product["id"])))
        else:
            kb.insert(InlineKeyboardButton(product["title"], callback_data=product_kb_cb.new(id=product["id"])))

    kb.add(InlineKeyboardButton("Cancel", callback_data="cancel"))
    return kb


@dp.message_handler(Text(equals="Menu"))
async def show_menu(message: Message):
    await message.answer(text="Here is our menu.",
                         reply_markup=generate_menu_keyboard())


products_show_kb_cb: CallbackData = CallbackData("products_show_kb_cb", "title", "product_id")


def get_add_to_cart_kb(product_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Add to cart", callback_data=products_show_kb_cb.new("cart", product_id))
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data=products_show_kb_cb.new("cancel", product_id))
        ]
    ])


@dp.callback_query_handler(product_kb_cb.filter())
async def cb_products_show_id(call: CallbackQuery, callback_data: dict):
    id = callback_data["id"]
    product = get_product(id)
    text = f"Title: {product['title']}\n" \
           f"Details: {product['details']}\n" \
           f"Price: {product['price']}\n"
    await bot.send_message(call.message.chat.id, text)
    await call.message.answer(f"Would you like to order this product?", reply_markup=get_add_to_cart_kb(product["id"]))
    await call.message.delete()


@dp.callback_query_handler(products_show_kb_cb.filter(title="cart"))
async def add_order(call: CallbackQuery, callback_data: dict):
    id = callback_data["product_id"]
    product = get_product(id)
    add_to_cart(id, call.from_user.id)
    await call.message.answer(f"You successfully added {product['title']} to cart")
    await call.message.delete()


@dp.callback_query_handler(text="cancel")
async def cancel_showing(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
