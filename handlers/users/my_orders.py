from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from utils.apirequests import get_order_history


def show_products_and_prices():
    reception = get_order_history()
    text = ''
    for i in range(len(reception)):
        orders = reception[i]
        if orders['orderCode'] == 0:
            status = "Your order is not ready yet"
        if orders['orderCode'] == 1:
            status = "Your order is ready"
        if orders['orderCode'] == 2:
            status = "Order is already given"
        if orders['orderCode'] == 3:
            status = "Order is not given"
        text = text + "Order Code: " + str(
            orders["orderCode"]) + '\n' + "Order Status: " + status + '\n' + "Products: \n"
        products = orders['products']
        for key, product in enumerate(products):
            text = text + product["title"] + " — " + str(product["price"]) + " KZT" + "\n"
        text = text + "\n\n"

    return text


@dp.message_handler(Text(equals="My orders 🧾"))
async def show_history(message: Message):
    text = show_products_and_prices()
    await message.answer(text)




