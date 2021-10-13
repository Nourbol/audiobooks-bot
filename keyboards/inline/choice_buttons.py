from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Potato", callback_data=buy_callback.new(
                title="Potato", price="200"
            )),
            InlineKeyboardButton(text="Bread", callback_data=buy_callback.new(
                title="Bread", price="50"
            )),
            InlineKeyboardButton(text="Salt", callback_data=buy_callback.new(
                title="Salt", price="200"
            )),
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data="cancel")
        ]
    ]
)