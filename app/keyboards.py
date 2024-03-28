from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


point = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Пройти викторину')],
    [KeyboardButton(text='Перейти на сайт'), KeyboardButton(text='Написать в тех.поддержку')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')

point_site = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Московский зоопарк', url='https://moscowzoo.ru/')]
])