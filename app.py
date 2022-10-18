from aiogram import executor

from loader import dp
import handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher): # Функция срабатывает при запуске бота, в неё мы «зашиваем» установку меню с командами
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)