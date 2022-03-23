import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('uz')
API_TOKEN = '5153518417:AAHq2PlunYkjpPzKvplKY_kTr-gyX_Sz6JE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

        await message.reply("Xush kelibsiz! Wikipedia botga")



@dp.message_handler()
async def wikiBot(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzudagi maqola topilmadi!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)