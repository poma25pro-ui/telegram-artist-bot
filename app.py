from flask import Flask, request
import telebot
import os

API_TOKEN = '8517313718:AAFBnyTrgU66yjLAImywD3GWpRPw4x9kpv4'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Бот-художник работает! Перейдите в Telegram."

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        json_data = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return 'OK'
    return 'Use POST request'

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "🎨 Привет! Я бот-художник!\nНапиши 'нарисуй' и что нарисовать!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text.lower()
    
    if 'нарисуй' in user_text:
        item = user_text.replace('нарисуй', '').strip()
        bot.reply_to(message, f"🖌️ Хорошо! Рисую: {item}\n(Функция реального рисования скоро будет добавлена!)")
    elif 'привет' in user_text:
        bot.reply_to(message, "👋 Привет! Я готов создавать картины по вашему запросу!")
    else:
        bot.reply_to(message, f"🤔 Вы сказали: '{message.text}'\nПопробуйте написать 'нарисуй' и что нарисовать!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
