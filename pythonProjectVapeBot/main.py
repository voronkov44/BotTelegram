import telebot
from telebot import types


bot = telebot.TeleBot('5897142092:AAGpNn97wry2bmBB1AvzUfJl_tsIvWTjvBM')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('➡️Другое')
    item2 = types.KeyboardButton('💨Каталог')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name}!', reply_markup = markup)


@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '➡️Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('❗️Скидки')
            item2 = types.KeyboardButton('✉️Сотрудничество')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, '➡️Другое:', reply_markup=markup)

        elif message.text == '💨Каталог':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Одноразовые устройства')
            item2 = types.KeyboardButton('Поды')
            item3 = types.KeyboardButton('Жидкость для пода')
            item4 = types.KeyboardButton('Испарители для пода')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, '💨Каталог:', reply_markup=markup)

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('➡️Другое')
            item2 = types.KeyboardButton('💨Каталог')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, '⬅️Назад:', reply_markup=markup)

        elif message.text == '✉️Сотрудничество':
            bot.send_message(message.chat.id, "По поводу сотрудничества писать: @keedsar")

        elif message.text == '❗️Скидки':
            bot.send_message(message.chat.id, "Скидка на первый заказ 5%🔥" "Приведи двух друзей и получи скидку 5%🔥" "Оставь отзыв и получи скидку 5% на следующий заказ🔥" "Скидки суммируются❗️")

        elif message.text == 'Одноразовые устройства':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('UDN-5000')
            item2 = types.KeyboardButton('UDN-5200')
            item3 = types.KeyboardButton('FB-8k')
            item4 = types.KeyboardButton('Chillax')
            back = types.KeyboardButton('💨Каталог')
            back2 = types.KeyboardButton('⏪Назад')
            markup.add(item1, item2, item3, item4, back, back2)

            bot.send_message(message.chat.id, 'Одноразовые устройства:', reply_markup=markup)

        elif message.text == '⏪Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('➡️Другое')
            item2 = types.KeyboardButton('💨Каталог')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, '⏪Назад:', reply_markup=markup)

        elif message.text == 'UDN-5000':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Информация UDN-5000')
            item2 = types.KeyboardButton('Вкусы UDN-5000')
            item3 = types.KeyboardButton('Фото UDN-5000')
            back3 = types.KeyboardButton('Одноразовые устройства')
            markup.add(item1, item2, item3, back3)

            bot.send_message(message.chat.id, 'UDN-5000:', reply_markup=markup)

        elif message.text == 'Информация UDN-5000':
            bot.send_message(message.chat.id,"Объем аккумулятора:600мАч; Объем жидкости:13мл; Количество затяжек:до 5000")

        elif message.text == 'Вкусы UDN-5000':
            bot.send_message(message.chat.id, "🍬Фруктовая конфета🍬; 🍌🍓Клубника банан🍓🍌; 🧊🍎Яблоко лёд🍎🧊; 🍹Личи маракуйя🍹; 🍇Алоэ виноград🍇")

        elif message.text == 'Фото UDN-5000':
            photo = open('udn5000.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'UDN-5200':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Информация UDN-5200')
            item2 = types.KeyboardButton('Вкусы UDN-5200')
            item3 = types.KeyboardButton('Фото UDN-5200')
            back3 = types.KeyboardButton('Одноразовые устройства')
            markup.add(item1, item2, item3, back3)

            bot.send_message(message.chat.id, 'UDN-5200:', reply_markup=markup)

        elif message.text == 'Информация UDN-5200':
            bot.send_message(message.chat.id,
                             "Объем аккумулятора:550мАч; Объем жидкости:12мл; Количество затяжек:до 5200")

        elif message.text == 'Вкусы UDN-5200':
            bot.send_message(message.chat.id, "🫐Черника гранат🫐; 🍑🥭Манго персик гуава 🥭🍑; 🧸Мармеладные мишки🧸; 🍍Ананас манго апельсин🍍; 🧊🍇Алоэ вингорад лёд🍇🧊; 🍧Клубничное мороженое 🍧")

        elif message.text == 'Фото UDN-5200':
            photo = open('udn5200.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'FB-8k':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Информация FB-8k')
            item2 = types.KeyboardButton('Вкусы FB-8k')
            item3 = types.KeyboardButton('Фото FB-8k')
            back3 = types.KeyboardButton('Одноразовые устройства')
            markup.add(item1, item2, item3, back3)

            bot.send_message(message.chat.id, 'FB-8k:', reply_markup=markup)

        elif message.text == 'Информация FB-8k':
            bot.send_message(message.chat.id, "Объем аккумулятора:800мАч; Объем жидкости:25мл; Количество затяжек:до 8000")

        elif message.text == 'Вкусы FB-8k':
            bot.send_message(message.chat.id, "🍉🥭Персик манго арбуз🥭🍉; 🧊🫐Черника лед🫐🧊; 🍹Маракуйя🍹; 🍓Клубника🍓; 🍓🫐Черника малина лед🫐🍓; 🍇Клюква виноград🍇")

        elif message.text == 'Фото FB-8k':
            photo = open('fb-8k.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'Chillax':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Информация Chillax')
            item2 = types.KeyboardButton('Вкусы Chillax')
            item3 = types.KeyboardButton('Фото Chillax')
            back3 = types.KeyboardButton('Одноразовые устройства')
            markup.add(item1, item2, item3, back3)

            bot.send_message(message.chat.id, 'Chillax:', reply_markup=markup)

        elif message.text == 'Информация Chillax':
            bot.send_message(message.chat.id, "Объем аккумулятора:600мАч; Объем жидкости:13мл; Количество затяжек:до 6000")

        elif message.text == 'Вкусы Chillax':
            bot.send_message(message.chat.id, "🫐Лесные ягоды🫐; 🧉Пинаколада🧉; 🍎Хрустящее яблоко🍎")

        elif message.text == 'Фото Chillax':
            photo = open('chillax.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)

















bot.polling(none_stop = True)