import time

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from utils.callbacks import MainCallback
from utils.keyboards import start_keyboard
from utils.states import BotStates

from handlers import pay

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "pay"))
async def get_paid(callback: types.CallbackQuery, state: FSMContext):
    """Формирование ссылки на оплату"""

    await callback.message.answer(
        f'Ссылка на оплату\n{await pay.pay_func(str(callback.from_user.username))}'
    )
    await state.set_state(BotStates.pay)
    time.sleep(2)
    await callback.message.answer(
        'Выберите команду или введите дату в формате дд.мм.гггг для добавления в таблицу',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)
