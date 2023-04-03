import os
import random
from aiogram import Bot, Dispatcher, types, executor
import confidentially as con # достаем токен
import button as bt # достаем кнопку

bot = Bot(token=con.TOKEN) # экземпляр класса бота
dp = Dispatcher(bot=bot) # экземпляр класса диспкчер

# старт
@dp.message_handler(commands=['start']) # декоратор сообщений
async def start_handler(message: types.Message): # обработка декоратора и приход сообщения
    user_name = message.from_user.full_name # узнаем имя кто написал
    await message.reply(f"Привет, {user_name}, я помогу тебе с мотивацией и пришлю тебе картинку! Напиши мне /picture или нажми кнопку ниже", reply_markup=bt.greet_kb) # высылаем сообщение как ответ

# картинка с кнопки
@dp.message_handler() # декоратор сообщения с кнопки
async def picture_sending(msg: types.Message): # обработка декоратора и приход сообщения
    photo = open('photo/' + random.choice(os.listdir('photo')), 'rb') # достаем рандомную фотку с папки
    await bot.send_photo(msg.from_user.id, photo) # присылаем фото пользвателю

# картинка с /picture
@dp.message_handler(commands=['picture'])# декоратор сообщения с /picture
async def picture_sending(msg: types.Message):# обработка декоратора и приход сообщения
    photo = open('photo/' + random.choice(os.listdir('photo')), 'rb')# достаем рандомную фотку с папки
    await bot.send_photo(msg.from_user.id, photo) # присылаем фото пользвателю

# запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp)