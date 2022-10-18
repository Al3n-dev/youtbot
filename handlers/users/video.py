from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states import Dowload

from pytube import YouTube
import os
import uuid

# скачивание видео
def dowload_video(url, type='audio'): #Функция download_video принимает в себя ссылку (формат строка) и тип
    yt = YouTube(url)  # Дальше создаем объект YouTube и передаем ссылку. После генерируем ID для файла.
    audio_id = uuid.uuid4().fields[-1]
    if type == 'audio':  # Дальше идет простая проверка - какой файл нам нужен на выходе
        yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
        return f"{audio_id}.mp3"
    elif type == 'video':
        return f"{audio_id}.mp4"

@dp.message_handler(Command('audio'))
async def start_dow(message: types.Message): # start_dow – отрабатывает при команде audio, отправляя сообщение с указанием
    await message.answer(text=f"Привет, {message.from_user.full_name}, скинь ссылку на видео и я отправлю ее тебе ввиде аудио.")
    await Dowload.dowload.set()


@dp.message_handler(state=Dowload.dowload)
async def dowload(message: types.Message, state: FSMContext): # срабатывает, когда у пользователя состояние dowload
    title = dowload_video(message.text)
    audio = open(f'audio/{title}', 'rb')
    await message.answer(text="Все скачалось держи аудио")
    try:
        await bot.send_audio(message.chat.id, audio)
        await bot.send_message(message.chat.id, text='')
    except:
        await message.answer(text="Файл слишком большой")
    os.remove(f'audio/{title}')
    await state.finish()

