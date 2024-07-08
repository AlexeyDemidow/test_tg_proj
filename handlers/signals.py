from aiogram import Router, Bot

from bot_settings import config

router = Router()


async def start_bot(bot: Bot):
    """Технический сигнал о запуске бота"""

    await bot.send_message(config.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    """Технический сигнал об остановке бота"""

    await bot.send_message(config.admin_id, text='Бот остановлен')
