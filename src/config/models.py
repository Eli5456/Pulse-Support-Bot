from pydantic import Field
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BotConfig(BaseSettings):
    """
    Bot config
    """

    token: SecretStr


class Messages(BaseSettings):
    notify_user_about_success_deliver: str = Field(
        default="✅ Ваше сообщение доставлено. Пожалуйста, ожидайте ответа."
    )
    help_message: str = Field(
        default="""
     <h1>
      👋 Здравствуйте!
      </h1>
      <p>
          Я могу передать администратору следующие типы сообщений: <b>текст, аудио, голосовые сообщения, изображения, файлы</b>.
      </p>

      <p>
       Просто отправьте мне сообщение и ждите ответа! 
      </p>
    """
    )
    help_message_admin: str = Field(
        default="""
     <h1>
      👋 Здравствуйте, Администратор!
      </h1>
      <p>
          Вы можете отвечать пользователям, используя функцию Reply (ответить) на их сообщения.
      </p>
      <p>
          Поддерживаются следующие типы сообщений: <b>текст, аудио, голосовые сообщения, изображения, файлы</b>.
      </p>
      <p>
          Для ответа пользователю просто нажмите Reply на его сообщение и напишите свой ответ.
      </p>
    """
    )
    notify_admin_about_success_answer: str = Field(default="✅ Ответ отправлен.")


class Errors(BaseSettings):
    unsupported_type: str = Field(
        default="❌ Неподдерживаемый тип сообщения.<br/>Пожалуйста, проверьте команду <b>/help</b>."
    )
    too_long_message_text: str = Field(default="❌ Слишком длинное текстовое сообщение.")
    too_long_message_caption: str = Field(default="❌ Слишком длинный текст подписи.")
    copy_message: str = Field(default="❌ Ошибка при копировании сообщения")
    extract_user_id: str = Field(default="❌ Ошибка при извлечении ID пользователя")
    chat_not_found: str = Field(
        default="❌ Ошибка доступа. Убедитесь, что вы начали диалог с ботом"
    )


class Config(BaseSettings):
    """
    All in one config
    """

    bot: BotConfig
    chat_id: str | int
    messages: Messages = Messages()
    errors: Errors = Errors()


__all__ = ["BotConfig", "Config"]
