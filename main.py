import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, \
   InlineKeyboardButton
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from app.keyboards import point, point_site
load_dotenv()


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer('Привет!\nЯ чат-бот Московского зоопарка!\nИ сейчас ты сможешь понять, какой ты зверь', reply_markup=point)


@dp.message(F.text == 'Перейти на сайт')
async def site_official(message: Message):
   await message.answer('Нажми чтобы перейти на сайт', reply_markup=point_site)

question = ['Где бы ты хотел жить?', 'Какая ваша любима еда?', 'На что вы обращаете внимание при первом знакомстве?', 'Что важнее всего для успеха?', 'Что вас успокаивает?', 'Как вы обычно проявляете злость?']

responses = {
   "У моря": 1, 'В Окружении цветов': 4, 'В тропической стране': 2, 'В горах': 5, "В лесу": 3,
   "Мясо": 2, 'Рыба': 1, 'Все равно': 3, "Овощи и фрукты": 5, 'Сладкое': 4,
   'На поведение': 1, "На тон голоса": 2, 'На запах': 3, 'На стиль одежды': 4, 'На жестикуляцию': 5,
   "Правильные знакомства и поддержка родных": 3, 'Сбор информации и умение ее применять': 4, 'Не стоять на месте и все время двигаться к цели': 1, 'Амбициозность и хитрость': 2, "Неординарные решения и умение адаптироваться": 5,
   "Приятная компания": 3, 'Принятие ванны': 1, 'Любимая музыка': 5, "Тихий домашний вечер в одиночестве": 2, 'Неспешная прогулка': 4,
   'Ухожу от обидчика': 4, "Говорю о своих чувствах": 1, 'Рву и мечу': 3, 'Отстаиваю свое мнение': 5, 'Срываетесь на крик': 2
}


@dp.message(F.text == 'Пройти викторину')
async def quiz_func(message: Message):
   answer_user = 0
   for quest in question:
      i=0
      for response in responses:
         point_response=ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text=response)]],
            resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню')
      await message.answer(quest, reply_markup=keyboard)


async def main():
   await dp.start_polling(bot)


if __name__ == '__main__':
   try:
      asyncio.run(main())
   except RuntimeError or KeyboardInterrupt or RuntimeError:
      print('Exit')
