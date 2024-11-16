TOKEN = "{{sensitive_data}}"

import telebot


# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! 👋 Я твой Telegram бот.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Это картинка! 🖼️")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.reply_to(message, f'Вы отправили текст: {message.text}')



bot.infinity_polling()