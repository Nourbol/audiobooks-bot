from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import authors_kb_cb


def authors_kb(authors):
    return InlineKeyboardMarkup(inline_keyboard=map(lambda author: [
        InlineKeyboardButton(text=author,
                             callback_data=authors_kb_cb.new(author=author))
    ], authors))