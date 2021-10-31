from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from utils.apirequests import get_order_history


def show_products_and_prices(user_id):
    reception = get_order_history(user_id)
    text = ''
    for i in range(len(reception)):
        orders = reception[i]
        if orders['orderStatus'] == 0:
            status = "In progress"
        if orders['orderStatus'] == 1:
            status = "Done. You can pick up it"
        if orders['orderStatus'] == 2:
            status = "Given"
        if orders['orderStatus'] == 3:
            status = "Canceled"
        text = text + "Order Code: " + str(
            orders["orderCode"]) + '\n' + "Order Status: " + status + '\n' + "Products: \n"
        products = orders['products']
        for key, product in enumerate(products):
            text = text + product["title"] + " — " + str(product["price"]) + " KZT" + "\n"
        text = text + "\n\n"

    return text


@dp.message_handler(Text(equals="My orders 🧾"))
async def show_history(message: Message):
    text = show_products_and_prices(message.from_user.id)
    await message.answer(text)




