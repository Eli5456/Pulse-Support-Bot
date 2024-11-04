import structlog
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.config import Messages

logger = structlog.stdlib.get_logger()
router = Router(name="misc")


@router.message(
    Command("start", "help"),
)  # type: ignore
async def start_help_handler(message: Message, messages: Messages, chat_id: int, **kwargs) -> None:
    """
    Handle /start or /help message
    :param message:
    :param messages:
    :param chat_id:
    :param kwargs:
    :return:
    """
    # Если сообщение от админа
    if message.from_user.id == chat_id:
        await message.answer(
            messages.help_message_admin,
            disable_web_page_preview=True,
        )
    else:
        await message.answer(
            messages.help_message,
            disable_web_page_preview=True,
        )


__all__ = ["router"]
