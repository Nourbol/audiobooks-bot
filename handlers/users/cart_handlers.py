from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import dp
from utils.apirequests import get_cart

cart_kb_cb: CallbackData = CallbackData("cart_kb_cb", "product_id")

order_creation_kb_cb: CallbackData = CallbackData("order_creation_kb_cb")


def get_cart_kb():
    kb = InlineKeyboardMarkup()
    products = get_cart()
    for key, product in enumerate(products):
        if product["title"] is None or product["title"] == '':
            continue
        if key % 2 == 0:
            kb.add(InlineKeyboardButton(product["title"], callback_data=cart_kb_cb.new(product_id=product["id"])))
        else:
            kb.insert(InlineKeyboardButton(product["title"], callback_data=cart_kb_cb.new(product_id=product["id"])))

    kb.add(InlineKeyboardButton("Cancel", callback_data="cancel"))
    return kb
    # product
    # Create order


@dp.message_handler(text="Cart")
async def cart_menu(message: Message):
    await message.answer(text="Here is your cart:",
                         reply_markup=get_cart_kb())
