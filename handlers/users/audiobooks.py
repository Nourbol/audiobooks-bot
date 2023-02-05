from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline.audiobooks import audiobooks_kb
from keyboards.inline.authors import authors_kb
from keyboards.inline.callback_data import authors_kb_cb, audiobooks_kb_cb
from loader import dp
from utils.apirequests import get_audiobooks_by_author, get_authors


@dp.message_handler(Text(equals="Authors"))
async def show_authors(message: Message):
    authors = map(lambda author: author['author'], get_authors())
    await message.answer(text='Here is available authors: ',
                         reply_markup=authors_kb(authors))


@dp.callback_query_handler(authors_kb_cb.filter())
async def show_author_audiobooks(call: CallbackQuery, callback_data: dict):
    audiobooks = get_audiobooks_by_author(callback_data['author'])
    await call.message.answer('Select an audiobook of the author ', reply_markup=audiobooks_kb(audiobooks))


@dp.callback_query_handler(audiobooks_kb_cb.filter())
async def show_audiobook(call: CallbackQuery, callback_data: dict):
    audiobook = callback_data['audiobook']
    await call.message.answer(f'Author: {audiobook["author"]}\n'
                              f'Title: {audiobook["title"]}\n'
                              f'Link: {audiobook["link"]}')


@dp.callback_query_handler(text="cancel")
async def cancel_showing(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
