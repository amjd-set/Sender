import telebot

API_TOKEN = '8015146138:AAHbXQmpMqGtCP7943gaj9EuEBjHuitL6mE'
YOUR_CHAT_ID = '7506329433'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    first_name = message.from_user.first_name.replace("<", "").replace(">", "")
    user_id = message.from_user.id
    name = f"<a href='tg://user?id={user_id}'>{first_name}</a>"
    text = f"رسالة من: {name}\n\n{message.text}"
    bot.send_message(chat_id=YOUR_CHAT_ID, text=text)
    bot.reply_to(message, 'تم إرسال رسالتك بنجاح!')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, '''مرحبا! أنا بوت لتحويل الرسائل.

ارسل رسالتك ليتم تحويلها. ''')

if __name__ == "__main__":
    bot.polling(none_stop=True)
