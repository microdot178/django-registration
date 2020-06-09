#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import os
import random
import time 

bot = telebot.TeleBot('- - - -');

@bot.message_handler(commands=["get"])

def get(message):
    bot.send_message(message.chat.id, 'скопируйте сюда ссылку, откуда скачать иконки')
    bot.register_next_step_handler(message, wgeticons)
    
def wgeticons(message):
    http = message.text
    bot.send_message(message.chat.id, 'минуточку...')
    random_zip_name=str(random.randint(0, 999))
    random_wget_dir_name=str(random.randint(1000, 1999))
    random_icon_dir_name=str(random.randint(2000, 2999))
    zipname = 'png' + random_zip_name
    icondirname = random_icon_dir_name
    wgetdirname = random_wget_dir_name
    os.system('wget -k -l 7 -p -E -r -nc {0} -P {1}'.format(http, wgetdirname))
    os.system('mkdir {1}'.format(wgetdirname, icondirname))
    a = 'find {0} -name "*.png" |'.format(wgetdirname) # ??? почему так
    b = ' parallel mv "{}"'                            # ??? некрасиво, я
    c = ' {0}'.format(icondirname)                     # ??? сам не могу
    abc = a + b + c                                    # ??? понять :c
    os.system(abc) 
    os.system('rm -r {0}'.format(wgetdirname))
    os.system('zip -qr {0} {1}'.format(zipname, icondirname))
    f = open('{0}.zip'.format(zipname), 'rb')
    msg = bot.send_document(message.chat.id, f, None)
    time.sleep(3)
    os.system('rm -r {0} {1}'.format(icondirname, wgetdirname))
    os.system('rm -r {0}'.format('{0}.zip'.format(zipname)))
    

if __name__ == '__main__':
    bot.infinity_polling()
    
bot.polling(none_stop=True, interval=0)
