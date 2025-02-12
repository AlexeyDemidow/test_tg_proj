from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    """Список команд бота"""

    commands = [
        BotCommand(
            command='start',
            description='Начать работу',
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
