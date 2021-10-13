from aiogram.types  import ReplyKeyboardMarkup, KeyboardButton

reception = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu'),
        ],
        [
            KeyboardButton(text='My orders'),
        ],
        [
            KeyboardButton(text='Cart'),
        ],
    ],
    resize_keyboard=True
)