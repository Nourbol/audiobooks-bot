from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from loader import dp, bot
from utils.apirequests import get_cart, get_product, delete_from_cart

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


cart_show_product_kb_cb: CallbackData = CallbackData("cart_show_product_kb_cb", "product_id")


def delete_from_cart_kb(product_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Удалить из корзины",
                                 callback_data=cart_show_product_kb_cb.new("delete", product_id))
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data=cart_show_product_kb_cb.new("cancel", product_id))
        ]
    ])


@dp.callback_query_handler(cart_kb_cb.filter())
async def kb_show_product_from_cart(call: CallbackQuery, callback_data: dict):
    id = callback_data["product_id"]
    product = get_product(id)
    text = f"Title: {product['title']}\n" \
           f"Category: {product['category']}\n" \
           f"Price: {product['price']}\n"
    await bot.send_message(call.message.chat.id, text)
    await call.message.answer(f"Would you like to delete {product['title']} from your cart?",
                              reply_markup=delete_from_cart_kb(product["id"]))
    await call.message.delete()


@dp.callback_query_handler(cart_show_product_kb_cb.filter(title="delete"))
async def delete_product_from_cart(call: CallbackQuery, callback_data: dict):
    id = callback_data["product_id"]
    delete_from_cart(id, call.from_user.id)
    await call.message.answer(f"You successfully deleted this product from the cart")
    await call.message.delete()
