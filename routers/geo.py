import time

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from utils.callbacks import MainCallback
from utils.keyboards import start_keyboard
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "geo"))
async def get_coordinates(callback: types.CallbackQuery, state: FSMContext):
    """Получение ссылки с координатами в Яндекс картах"""

    await callback.message.answer(
        'Координаты адреса "Республика Беларусь, Гомельская область, город Светлогорск, улица Ленина дом 1"'
        'https://yandex.by/maps/26004/svetlogorsk/house/ZkAYcQFgQEQBQFtofXpzdnxgZw==/?ll=29.769828%2C52.626616&z=15.75'
    )
    await state.set_state(BotStates.geo)
    time.sleep(2)
    await callback.message.answer(
        'Выберите команду или введите дату в формате дд.мм.гггг для добавления в таблицу',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)
