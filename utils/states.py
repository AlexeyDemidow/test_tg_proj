from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):
    """Все состояния бота"""

    start = State()
    geo = State()
    pic = State()
    table = State()
    pay = State()
