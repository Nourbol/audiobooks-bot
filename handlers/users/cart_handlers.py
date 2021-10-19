from aiogram.types import Message
from aiogram.utils.callback_data import CallbackData

from loader import dp

cart_kb_cb: CallbackData = CallbackData("cart_kb_cb", "product_id")

order_creation_kb_cb: CallbackData = CallbackData("order_creation_kb_cb")


def get_cart_kb():
    pass
    # product
    # Create order


@dp.message_handler(text="Cart")
async def cart_menu(message: Message):
    await message.answer("Hello")
