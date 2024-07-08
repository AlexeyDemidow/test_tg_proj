from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import MainCallback
from bot_settings import config


async def start_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура основного меню"""

    skb = InlineKeyboardBuilder()
    skb.button(
        text='Ленина 1',
        callback_data=MainCallback(mcb='geo').pack(),
    )
    skb.button(
        text='Оплата',
        callback_data=MainCallback(mcb='pay').pack(),
    )
    skb.button(
        text='Картинка',
        callback_data=MainCallback(mcb='pic').pack(),
    )
    skb.button(
        text='Ячейка А2 из таблицы',
        callback_data=MainCallback(mcb='table').pack(),
    )
    skb.button(
        text='Ссылка на таблицу',
        url=config.table_link,
    )
    skb.adjust(1)

    return skb.as_markup(resize_keyboard=True)
