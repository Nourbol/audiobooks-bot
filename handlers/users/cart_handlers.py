from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from loader import dp, bot
from utils.apirequests import get_cart, get_product, delete_from_cart, create_order

cart_kb_cb: CallbackData = CallbackData("cart_kb_cb", "product_id")

order_creation_kb_cb: CallbackData = CallbackData("order_creation_kb_cb", "title")

yes_no_kb_cb: CallbackData = CallbackData("yes_no_kb_cb", "yes_no")


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
    confirmation = State()


@dp.callback_query_handler(order_creation_kb_cb.filter(title="order"))
async def make_order(call: CallbackQuery):
    await OrderCreationState.phone_number.set()
    await call.message.answer("Now enter your phone number starting with 8")


def is_phone_correct(phone_number: str):
    return phone_number.isdigit() \
           and len(phone_number) == 11 \
           and phone_number[0] == '8'


@dp.message_handler(state=OrderCreationState.phone_number)
async def phone_input(message: Message, state: FSMContext):
    if not is_phone_correct(message.text):
        await message.answer("Phone number is incorrect\n"
                             "It must be a number with 11 digits and starts with \'8\'\n"
                             "Like 87071112233")
        return

    await state.update_data(phone=message.text)
    await OrderCreationState.confirmation.set()
    products = get_cart(message.from_user.id)
    total = get_total_price(products)
    await message.answer(f"Are you really want to buy {len(products)}\n"
                         f"With total price: {total}?", reply_markup=get_yes_no_kb())


@dp.callback_query_handler(yes_no_kb_cb.filter(), state=OrderCreationState.confirmation)
async def awaiting(call: CallbackQuery, state: FSMContext, callback_data: dict):
    if callback_data["yes_no"] == "no":
        await call.message.answer("Canceled")
        await state.finish()
        return

    phone_number = (await state.get_data())["phone"]
    create_order(call.from_user.id, phone_number)
    await state.finish()
    await call.message.answer("You create an order")


def get_total_price(products):
    total = 0
    for product in products:
        total += product['price']
        return total


@dp.message_handler(text="Cart")
async def cart_menu(message: Message):
    products = get_cart(message.from_user.id)

    await message.answer(text=f"Total: {get_total_price(products)} KZT\n"
                              "Here is your cart:",
                         reply_markup=get_cart_kb(products))


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


@dp.callback_query_handler(cart_show_product_kb_cb.filter(product_id="delete"))
async def delete_product_from_cart(call: CallbackQuery, callback_data: dict):
    id = callback_data["product_id"]
    delete_from_cart(id, call.from_user.id)
    await call.message.answer(f"You successfully deleted this product from the cart")
    await call.message.delete()
