from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = 'сюда ваш токен'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML) # Дальше создаем объект бота - указываем токен и тип выделения текста, как в html

storage = MemoryStorage() # Создаем объект для хранения в оперативной памяти

dp = Dispatcher(bot, storage=storage) # Дальше все передаем в диспетчер

