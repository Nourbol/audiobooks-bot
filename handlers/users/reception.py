from aiogram.utils.markdown import bold

from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import reception
from aiogram.dispatcher.filters import Command, Text, CommandStart


@dp.message_handler(CommandStart())
async def show_menu(message: Message):
    await message.answer("Hello! 👋\n" + 'I am Ashana AITU bot 👩‍🍳'
                         + f"\nI was created for the ICT endterm project. \n"
                           f"You can make orders in AITU's canteen using this bot!",
                         reply_markup=reception)


@dp.message_handler(Text(equals="main_menu"))
async def get_direction(message: Message):
    await message.answer(f"Here is our menu 📔 \n"
                         f"What would you like to order?",
                         reply_markup=show_menu()
                         )
