import time

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message

from utils.keyboards import start_keyboard
from utils.states import BotStates

from handlers import table


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    """Отображение меню после команды start"""

    await message.answer(
        'Выберите команду или введите дату в формате дд.мм.гггг для добавления в таблицу',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)


@router.message(BotStates.start)
async def add_date(message: Message, state: FSMContext):
    """Ввод и проверка даты, и добавление в таблицу если дата верна"""

    await table.add_data(message.text)
    await message.answer('Дата верна')
    await state.set_state(BotStates.table)
    time.sleep(3)
    await message.answer(
        'Выберите команду или введите дату в формате дд.мм.гггг для добавления в таблицу',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)
