from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import os

API_TOKEN = os.getenv('API_TOKEN')  # Токен берется из переменной окружения

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("🔧 Услуги"), KeyboardButton("📍 Адрес"))
main_kb.add(KeyboardButton("🗓 Запись"), KeyboardButton("❓ Вопрос"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот Cartweaker. Чем могу помочь?", reply_markup=main_kb)

@dp.message_handler(lambda msg: "услуги" in msg.text.lower())
async def show_services(message: types.Message):
    text = (
        "📋 Услуги Cartweaker:\n"
        "- 🚫 EGR OFF — от £100\n"
        "- ♻️ DPF OFF — от £120\n"
        "- 💨 Stage1 — от £150\n"
        "- 🔒 IMMO OFF — от £80\n"
        "\nДля точной оценки отправьте VIN или модель авто."
    )
    await message.answer(text)

@dp.message_handler(lambda msg: "адрес" in msg.text.lower())
async def show_address(message: types.Message):
    await message.answer("📍 Мы находимся в Кембридже. Работаем Пн–Сб с 09:00 до 18:00. Телефон: +44 0000 000000")

@dp.message_handler(lambda msg: "запись" in msg.text.lower())
async def handle_booking(message: types.Message):
    await message.answer("🗓 Для записи отправьте: имя, авто, VIN и удобное время.")

@dp.message_handler(lambda msg: "вопрос" in msg.text.lower())
async def handle_questions(message: types.Message):
    await message.answer("❓ Напишите ваш вопрос. Я постараюсь помочь или свяжу с мастером.")

@dp.message_handler()
async def fallback(message: types.Message):
    if len(message.text) == 7 and message.text[0].isalpha():
        await message.answer("🔍 Принял номер авто. Проверка в демо-режиме. Скоро подключим DVLA API.")
    else:
        await message.answer("🤖 Я не понял запрос. Нажмите кнопку или напишите ключевое слово: 'услуги', 'адрес', 'запись', 'вопрос'.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)