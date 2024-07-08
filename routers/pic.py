import time

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import URLInputFile

from bot import bot
from utils.callbacks import MainCallback
from utils.keyboards import start_keyboard
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "pic"))
async def get_picture(callback: types.CallbackQuery, state: FSMContext):
    """Картинка с текстом"""

    photo = URLInputFile(
        'https://koshka.top/uploads/posts/2021-11/thumbs/1636850985_38-koshka-top-p-koshki-kotik-v-shapochke-57.jpg',
        filename='img1.jpg'
    )
    await bot.send_photo(callback.from_user.id, photo, caption='Котик')
    await state.set_state(BotStates.pic)
    time.sleep(2)
    await callback.message.answer(
        'Выберите команду или введите дату в формате дд.мм.гггг для добавления в таблицу',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)
