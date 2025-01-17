from aiogram import Bot, Dispatcher, types
import asyncio
import importlib
import os
# import requests

Token = "8070766816:AAE-5OJFJjvs-dVQ1CsvYlbmZ1cLcAJd7QM"
chenal_name = ""
bot = Bot(token=Token)
dp = Dispatcher()
user_data = {}
project_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(project_dir, "images")


@dp.message()
async def message_handler(message: types.Message):
    user_id = message.from_user.id
    if message.text == "/start":
        await welcome(message)
    elif "language" not in user_data[user_id]:
        await check_lang(message)
    elif "phone" not in user_data[user_id]:
        await check_sms(message)
    elif 'state' not in user_data[user_id]:
        await choice_menu(message)
    elif "none" in user_data[user_id]['state']:
        await show_menu(message)
    elif 'categories' in user_data[user_id]['state']:
        await show_category(message)
    elif 'items' in user_data[user_id]['state']:
        await show_items(message)
    elif 'item' in user_data[user_id]['state']:
        await preview_items(message)
    elif message.text == user_data[user_id]["lang_module"].text_about:
        await show_about(message)


async def welcome(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="Русский 🇷🇺"),
         types.KeyboardButton(text="Ўзбекча 🇺🇿")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"Здравствуйте! Добро пожаловать в наш бот! \n"
                         f"Давайте для начала выберем язык обслуживания!", reply_markup=keyboard)


def select_lang(lang):
    if lang == 'Русский 🇷🇺':
        lang = 'ru'
    elif lang == 'Ўзбекча 🇺🇿':
        lang = 'uz'
    else:
        lang = 'uz'
    return lang
