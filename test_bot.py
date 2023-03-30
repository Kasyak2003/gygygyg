import telebot
from telebot import types

bot = telebot.TeleBot('6216252013:AAEc1I3Zzp_Ar_3tmscyb2ZXxJnP0WxEu4s')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Завести рейтинговую карту')
        btn2 = types.KeyboardButton('Моя статистика')
        btn3 = types.KeyboardButton('Рейтинг')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup) #ответ бота
    
    elif message.text == 'Завести рейтинговую карту':
    bot.send_message(message.from_user.id, 'завести свою рейтинговую карту вы можете по ' + '[ссылке](https://docs.google.com/forms/d/e/1FAIpQLSeiT7VGiQoAkgHjFBOfMyY_sfeXjNBz7MDUndTfGJMxi5b9Vw/viewform?fbzx=-8086485185386014541)', parse_mode='Markdown')

    elif message.text == 'Моя статистика':
    bot.send_message(message.from_user.id, 'Свою статистику вы можете узнать у администратора на ресепшене')

    elif message.text == 'Рейтинг':
    bot.send_message(massage.from_user.id, 'добавим попозже')

bot.polling(none_stop=True, interval=0)
