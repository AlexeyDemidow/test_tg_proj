from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # SecretStr для токена бота
    bot_token: SecretStr
    admin_id: int
    table_link: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


# При импорте файла сразу создастся и провалидируется объект конфига, который можно далее импортировать
config = Settings()
