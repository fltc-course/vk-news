from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi!\nCheck /help command!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text('I can answer the following commands:',
               '/put_link', '/links', '/start', '/help', sep='\n')
    await message.reply(msg)


@dp.message_handler(commands=['put_link'])
async def link_save_command(message: types.Message):
    link = message.get_args()
    await message.reply("Link added")


@dp.message_handler(commands=['links'])
async def show_links(message: types.Message):
    await message.reply("Links from BD")


if __name__ == '__main__':
    executor.start_polling(dp)
