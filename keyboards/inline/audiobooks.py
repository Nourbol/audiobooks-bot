from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import audiobooks_kb_cb


def audiobooks_kb(audiobooks):
    return InlineKeyboardMarkup(inline_keyboard=map(lambda audiobook: [
        InlineKeyboardButton(text=audiobook['title'],
                             callback_data=audiobooks_kb_cb.new(audiobook=audiobook))
    ], audiobooks))
