from aiogram.dispatcher.filters.state import StatesGroup, State


class orders(StatesGroup):
    order = State()
