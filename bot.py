from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text

from config import *
from bot_func.posts import *

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi!\nCheck /help command!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text('I can answer the following commands:',
               '/start', '/get_posts', '/help', sep='\n')
    await message.reply(msg)


# @dp.message_handler(commands=['put_link'])
# async def link_save_command(message: types.Message):
#     link = message.get_args()
#     await message.reply("Link added")
#
#
# @dp.message_handler(commands=['links'])
# async def show_links(message: types.Message):
#     await message.reply("Links from BD")


@dp.message_handler(commands=['get_posts'])
async def get_posts_handler(message: types.Message):
    posts = get_posts(VK_TOKEN, START_TIME)
    for post in posts:
        try:
            if "attachments" not in post or len(post["attachments"]) == 0:
                await message.answer(text=post["text"])
            else:
                media = types.MediaGroup()
                for attachment in post["attachments"]:
                    caption = None
                    if len(media.to_python()) == 0:
                        caption = post["text"]
                    try:
                        media_attach_file(media, attachment, VK_TOKEN, caption)
                    except:
                        print("error")
                        continue
                if len(media.to_python()) != 0:
                    await message.answer_media_group(media)
        except:
            continue


if __name__ == '__main__':

    executor.start_polling(dp)
