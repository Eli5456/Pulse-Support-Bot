from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram.types import BotCommandScopeDefault
from sulguk import AiogramSulgukMiddleware
from sulguk import SULGUK_PARSE_MODE

from src.config import BotConfig


async def setup_bot(config: BotConfig) -> Bot:
    """
    :param config:
    :return:
    """
    bot: Bot = Bot(
        token=config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=SULGUK_PARSE_MODE),
    )

    # https://github.com/Tishka17/sulguk#example-for-aiogram-users
    bot.session.middleware(AiogramSulgukMiddleware())

    user_commands = [
        BotCommand(command="help", description="Как использовать бот"),
    ]

    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    return bot


__all__ = ["setup_bot"]
