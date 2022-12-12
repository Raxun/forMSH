import datetime
import telebot
from telebot import types
from data import db_session
from data.Users import User


bot = telebot.TeleBot('5831975125:AAFG2Y4URAaUcmYOdTXwSdQSL0FgNHNlA6M', parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("5")
    btn2 = types.KeyboardButton("6")
    btn2 = types.KeyboardButton("7")
    btn3 = types.KeyboardButton("8")
    btn4 = types.KeyboardButton("9")
    btn5 = types.KeyboardButton("10")
    btn6 = types.KeyboardButton("11")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, )
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Укажи свой класс😉".format(message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    sp = ["Технологический", "Химико-биологический", "Лингвистический", "Гуманитарный",
          "Социально-экономический", "Нет"]
    db_session.global_init('db/users.db')
    db_sess = db_session.create_session()
    try:
        if 5 <= int(message.text) <= 11:
            pass
    except ValueError:
        try:
            if str(message.text) in sp:
                pass
        except ValueError:
            message.text = 0
    if db_sess.query(User.user_id).filter(User.user_id == int(message.from_user.id)).first() is None:
        if 5 <= int(message.text) <= 11:
            s1 = User()
            s1.user_id = int(message.from_user.id)
            s1.clas = int(message.text)
            s1.prof = None
            db_sess.add(s1)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Технологический")
            btn2 = types.KeyboardButton("Химико-биологический")
            btn3 = types.KeyboardButton("Лингвистический")
            btn4 = types.KeyboardButton("Гуманитарный")
            btn5 = types.KeyboardButton("Социально-экономический")
            btn6 = types.KeyboardButton("Нет")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.chat.id, 'Отлично! Теперь введи свой профиль', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Бот предназначен для обучающихся 5-11 классов')
            send_welcome(message)
    elif str(message.text) in sp:
        if db_sess.query(User.prof).filter(User.user_id == int(message.from_user.id)).first()[0] is None:
            s1 = db_sess.query(User).filter(User.user_id == int(message.from_user.id)).first()
            s1.prof = str(message.text)
            db_sess.add(s1)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Ваш класс и профиль")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Записал😉', reply_markup=markup)
        else:
            pass
    elif str(message.text) == "Ваш класс и профиль":
            clas = db_sess.query(User.clas).filter(User.user_id == int(message.from_user.id)).first()[0]
            prof = db_sess.query(User.prof).filter(User.user_id == int(message.from_user.id)).first()[0]
            bot.send_message(message.chat.id,
                             text=f"{message.from_user.first_name} вы в {clas[0]} классе. Ваш профиль {prof}")

    db_sess.commit()


bot.polling(none_stop=True)
