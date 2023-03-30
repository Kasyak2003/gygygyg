
    elif message.text == 'Моя статистика':
    bot.send_message(message.from_user.id, 'Свою статистику вы можете узнать у администратора на ресепшене')

    elif message.text == 'Рейтинг':
    bot.send_message(massage.from_user.id, 'добавим попозже')

bot.polling(none_stop=True, interval=0)
