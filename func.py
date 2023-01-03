from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove, bot
from sql_cons import *
import sqlite3
from datetime import date
today = date.today()
import random
from time import sleep

def start(update, context):
    user_id = update.message.chat_id
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
    connect.commit()
    context.bot.send_message(chat_id=user_id, text=dct[2][14])
    sleep(2)
    context.bot.send_message(chat_id=user_id, text=dct[2][0])
    cur.execute(first_insert.format(user_id, 2))
    connect.commit()


def audio(update, context):
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    connect.commit()
    user_id = update.message.chat_id

    context.bot.send_message(chat_id=user_id, text=dct[2][13])



def next_func(update, context):
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    connect.commit()
    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name

    stage_ = cur.execute(select_Stage.format(user_id)).fetchall()
    a_name = cur.execute(select_Ism.format(user_id)).fetchall()
    s_name = cur.execute(select_Familiya.format(user_id)).fetchall()
    num = cur.execute(select_Telefon.format(user_id)).fetchall()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    connect.commit()

    try:
        stage_ = stage_[0][0]
        num = num[0][0]
        a_name = a_name[0][0]
        s_name = s_name[0][0]
        TG_ID=TG_ID[0][0]

    except Exception:
        pass
    message = update.message.text
    message = str(message)

    if message == "delete_all":
        cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text="Uchdi xammasi bratiwka")
    if stage_ == 1 and message == 'РУС🇷🇺':
        knopka_lang = [
            KeyboardButton(text='РУС🇷🇺'),
            KeyboardButton(text='УЗБ🇺🇿')
        ]
        context.bot.send_message(chat_id=user_id, text=dct[2][0], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardRemove([knopka_lang], resize_keyboard=True))

        cur.execute(upd_Lang.format(1, user_id))
        cur.execute(upd_Stage.format(2, user_id))
        connect.commit()

    if stage_ == 1 and message == 'УЗБ🇺🇿':
        knopka_lang = [
            KeyboardButton(text='РУС🇷🇺'),
            KeyboardButton(text='УЗБ🇺🇿')
        ]
        context.bot.send_message(chat_id=user_id, text=dct[2][0], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardRemove([knopka_lang], resize_keyboard=True))


        cur.execute(upd_Stage.format('{}', user_id).format(2))
        connect.commit()

    if stage_ == 2 and " " in message and int(len(message)) >= 7:
        print('12321dfeferw')
        message_list = message.split()
        familiya = message_list[0]
        ism = message_list[1]

        cur.execute(upd_Familiya.format(familiya, user_id))

        cur.execute(upd_Ism.format(ism, user_id))

        cur.execute(upd_Stage.format('{}', user_id).format(3))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[2][1], parse_mode='Markdown')

    # betda nomer tekshiradi va kimligini soridi

    if stage_ == 3 and len(str(message)) == 9:

            message = int(message)
            cur.execute(upd_Telefon.format(message, user_id))
            cur.execute(upd_Stage.format(4, user_id))

            connect.commit()

            context.bot.send_message(chat_id=user_id, text=dct[2][2])

    if stage_ == 3 and len(str(message)) != 9:
        try:

           f= int(message)
           f+1
           context.bot.send_message(chat_id=user_id, text= dct[2][1] , parse_mode='Markdown')
        except Exception:
            context.bot.send_message(chat_id=user_id, text=dct[2][1], parse_mode='Markdown')

