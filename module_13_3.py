import telebot
from telebot.types import Message

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(message.chat.id, 'Привет! Я бот помогающий твоему здоровью.')

@bot.message_handler(func=lambda message: True)
def all_messages(message: Message):
    bot.send_message(message.chat.id, 'Введите команду /start, чтобы начать общение.')

print("Bot is running...")
bot.infinity_polling()

