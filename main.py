from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import config
from config import load_config, Config

dp: Dispatcher = Dispatcher()
config: Config = config.load_config()
Bot: Bot = Bot(token = config(config.tg_bot.token, parse_mode = 'HTML'))

@dp.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text='Я бот, демонстрирующий '
                 'как работает разметка. Отправь команду '
                 'из списка ниже:\n\n'
                 '/html - пример разметки с помощью HTML\n'
                 '/markdownv2 - пример разметки с помощью MarkdownV2\n'
                 '/noformat - пример с разметкой, но без указания '
                 'параметра parse_mode')

@dp.message(Command(commands='html'))
async def process_html_command(message: Message):
    await message.answer(text='Это текст, демонстрирующий '
                 'как работает HTML-разметка:\n\n'
                 '<b>Это жирный текст</b>\n'
                 '<i>Это наклонный текст</i>\n'
                 '<u>Это подчеркнутый текст</u>\n'
                 '<span class="tg-spoiler">А это спойлер</span>\n\n'
                 'Чтобы еще раз посмотреть список доступных команд - '
                 'отправь команду /help', parse_mode='HTML')

