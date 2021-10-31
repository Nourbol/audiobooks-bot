import datetime
import logging
import time

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from loader import dp, bot
from utils.apirequests import get_cart, get_product, delete_from_cart, create_order, send_code

cart_kb_cb: CallbackData = CallbackData("cart_kb_cb", "product_id")

order_creation_kb_cb: CallbackData = CallbackData("order_creation_kb_cb", "title")

yes_no_kb_cb: CallbackData = CallbackData("yes_no_kb_cb", "yes_no")

set_down_order_cb: CallbackData = CallbackData("set_down_order_cb", "minutes")


def get_set_down_order_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("As soon as possible", callback_data=set_down_order_cb.new(minutes=0))
    ], [
        InlineKeyboardButton("In 30 min", callback_data=set_down_order_cb.new(minutes=30)),
        InlineKeyboardButton("In 60 min", callback_data=set_down_order_cb.new(minutes=60))
    ]
    ])


def get_yes_no_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("Yes", callback_data=yes_no_kb_cb.new(yes_no="yes")),
        InlineKeyboardButton("No", callback_data=yes_no_kb_cb.new(yes_no="no"))
    ]])


def get_cart_kb(products):
    kb = InlineKeyboardMarkup()
    for key, product in enumerate(products):
        if product["title"] is None or product["title"] == '':
            continue
        if key % 2 == 0:
            kb.add(InlineKeyboardButton(product["title"], callback_data=cart_kb_cb.new(product_id=product["id"])))
        else:
            kb.insert(InlineKeyboardButton(product["title"], callback_data=cart_kb_cb.new(product_id=product["id"])))

    kb.add(InlineKeyboardButton("Make Order", callback_data=order_creation_kb_cb.new("order")))
    kb.add(InlineKeyboardButton("Cancel", callback_data=order_creation_kb_cb.new("cancel")))
    return kb
    # product
    # Create order


class OrderCreationState(StatesGroup):
    phone_number = State()
    phone_confirmation = State()
    deliveryTime = State()
    confirmation = State()


@dp.callback_query_handler(order_creation_kb_cb.filter(title="order"))
async def make_order(call: CallbackQuery):
    await OrderCreationState.phone_number.set()
    await call.message.answer(f"Please, enter your phone number! \n"
                              f"Example: 87071112233")


def is_phone_correct(phone_number: str):
    return phone_number.isdigit() \
           and len(phone_number) == 11 \
           and phone_number[0] == '8'


@dp.message_handler(state=OrderCreationState.phone_number)
async def phone_input(message: Message, state: FSMContext):
    phone = message.text
    if not is_phone_correct(phone):
        await message.answer("Phone number is incorrect\n"
                             "The phone number must be 11 digits long and start with \'8\'\n"
                             "Example: 87071112233")
        return

    await state.update_data(phone=phone)

    code = send_code(phone)
    await state.update_data(confirmation_code=code)
    await state.update_data(attempts=0)

    await OrderCreationState.phone_confirmation.set()
    await message.answer(f"I've sent confirmation code to your phone number\n"
                         f"Please, type code bellow")


@dp.message_handler(state=OrderCreationState.phone_confirmation)
async def phone_confirmation(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text != data["confirmation_code"]:
        attempts = data["attempts"]
        if attempts == 3:
            await message.answer("Invalid code, order is canceled")
            await state.finish()
            return

        await state.update_data(attempts=attempts + 1)
        await message.answer(f"Code is invalid, try again [{attempts + 1}/3]")
        return

    await OrderCreationState.deliveryTime.set()
    await message.answer("Perfect! Now you can set down your order", reply_markup=get_set_down_order_kb())


@dp.callback_query_handler(set_down_order_cb.filter(), state=OrderCreationState.deliveryTime)
async def delivery_time_set(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await state.update_data(minutes=callback_data["minutes"])

    await OrderCreationState.confirmation.set()
    products = get_cart(call.from_user.id)
    total = get_total_price(products)
    await call.message.answer(f"Are you really want to buy {len(products)} products\n"
                              f"with total price {total} KZT?", reply_markup=get_yes_no_kb())


@dp.callback_query_handler(yes_no_kb_cb.filter(), state=OrderCreationState.confirmation)
async def awaiting(call: CallbackQuery, state: FSMContext, callback_data: dict):
    if callback_data["yes_no"] == "no":
        bot.answer_callback_query(call.id, "You canceled the order!", show_alert=True)
        await state.finish()
        return

    data = await state.get_data()
    phone_number = data["phone"]
    minutes = int(data["minutes"])

    date = int(time.mktime(datetime.datetime.now().timetuple()))
    date += minutes * 60

    result = create_order(call.from_user.id, phone_number, date)

    await state.finish()

    if result == "ok":
        await call.message.answer(f"The order has been created!\n"
                                  f"You can pick up your order in a few minutes")
    else:
        await call.message.answer(f"Error in order creating, try one more time")
        print("error: " + result)


def get_total_price(products):
    total = 0
    for product in products or []:
        total += product['price']
        return total


@dp.message_handler(text="Cart 🛒")
async def cart_menu(message: Message):
    products = get_cart(message.from_user.id)

    await message.answer(text=f"Total price: {get_total_price(products)} KZT\n"
                              "Here is your cart:",
                         reply_markup=get_cart_kb(products))


show_product_kb_cb: CallbackData = CallbackData("show_product_kb_cb", "title", "product_id")


def delete_from_cart_kb(product_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Delete from the cart",
                                 callback_data=show_product_kb_cb.new("delete", product_id))
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data=show_product_kb_cb.new("cancel", product_id))
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
                              reply_markup=delete_from_cart_kb(product['id']))
    await call.message.delete()


@dp.callback_query_handler(show_product_kb_cb.filter(title="delete"))
async def delete_product_from_cart(call: CallbackQuery, callback_data: dict):
    id = callback_data['product_id']
    delete_from_cart(id, call.from_user.id)
    await call.message.answer(f"This product has been deleted from the cart!")
    await call.message.delete()
