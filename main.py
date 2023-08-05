import asyncio
import logging
from aiogram import executor
from googletrans import Translator
from aiogram import Bot, Dispatcher, types 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from googletrans import Translator

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6683405646:AAH14O-bxWUSZiB-Sec9OelrJuAbYuxsL4E")
dp = Dispatcher(bot, storage=MemoryStorage())
      
channel_id = "@Mutaallim_arabic"
channel_link = "https://t.me/Mutaallim_arabic"

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    print(chat_member['status'],'000000000')
    if chat_member['status'] == 'left':
        button_join = types.InlineKeyboardButton(text="Kanalga qo`shilish", url=channel_link)
        keyboard = types.InlineKeyboardMarkup().add(button_join)
        await message.reply("Iltimos, botimizdan foydalanish uchun kanalga qo`shiling.\nSo`ngra tarjimon botimizdan bemalol foydalanishingiz mumkin.", reply_markup=keyboard)
        return
    else:
        await message.reply("Assalomu alaykum! Botimizga xush kelibsiz!")
    
    
    # Translation code 

@dp.message_handler()
async def translate(message: types.Message, state: FSMContext):
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if chat_member['status'] == 'left':
        button_join = types.InlineKeyboardButton(text="Kanalga qo`shilish", url=channel_link)
        keyboard = types.InlineKeyboardMarkup().add(button_join)
        await message.reply("Iltimos, botimizdan foydalanish uchun kanalga qo`shiling.", reply_markup=keyboard)
        return
        
    def translat(matn):
        translator = Translator()
        # matn tilini aniqlaymiz
        til = translator.detect(matn).lang
        if til == "ar":  # agar til ingliz tilda boʻlsa
            return translator.translate(matn, dest="uz").text
        else:
            return translator.translate(matn, dest="ar").text

    text = message.text

    await message.reply(translat(text))

if __name__ == '__main__':
    executor.start_polling(dp)