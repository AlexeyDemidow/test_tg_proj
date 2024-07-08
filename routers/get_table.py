import time

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from utils.callbacks import MainCallback
from utils.keyboards import start_keyboard
from utils.states import BotStates

from handlers import table

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "table"))
async def get_cell(callback: types.CallbackQuery, state: FSMContext):
    """Получение значения ячейки А2 таблицы"""

    data = await table.get_data()
    await callback.message.answer(data)
    await state.set_state(BotStates.table)
    time.sleep(2)
    await callback.message.answer(
        'Выберите команду или введите дату в формате дд.мм.гггг для добавления в таблицу',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)
