from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.utils.callback_data import CallbackData

from loader import dp
from utils.apirequests import get_orders

product_kb_cb: CallbackData = CallbackData("product_kb_cb", "title")


def generate_menu_keyboard():
    kb = InlineKeyboardMarkup()
    orders = get_orders()
    for key, order in enumerate(orders):
        if order["title"] is None or order["title"] == '':
            continue
        if key % 2 == 0:
            kb.add(InlineKeyboardButton(order["title"], callback_data=product_kb_cb.new(order["title"])))
        else:
            kb.insert(InlineKeyboardButton(order["title"], callback_data=product_kb_cb.new(order["title"])))

    kb.add(InlineKeyboardButton("Cancel", callback_data="cancel"))
    return kb


@dp.message_handler(Text(equals="My orders"))
async def show_order_list(message: Message):
    await message.answer(text="Here is our menu.",
                         reply_markup=generate_menu_keyboard())
