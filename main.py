import telebot
import requests

API_TOKEN = '7780281238:AAHPP2lQ2as8HB7krpnaCe5L1rjneB_-dJM'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Kirim /analisa untuk mendapatkan analisa pasar.")

@bot.message_handler(commands=['analisa'])
def handle_analisa(message):
    bot.send_chat_action(message.chat.id, 'typing')
    analysis_text = get_fake_analysis()
    bot.reply_to(message, analysis_text)

def get_fake_analysis():
    return ("📊 *Analisa BTC/USD:*\n"
            "RSI: 38 | MACD: Bullish Cross\n"
            "Rekomendasi: Buy limit di support 60.000\n"
            "_(Data simulasi – nanti bisa real)_")

bot.polling(non_stop=True)
