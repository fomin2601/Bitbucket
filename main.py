import telebot
import os
import logging
import datetime
import PIL

BOT_TOKEN = os.getenv('BITBUCKET_BOT_TOKEN_TEST_TASK')
IMAGES_PATH = 'images/'

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(
    level=logging.DEBUG,
    format=''
)


def gen_share_markup():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    button1 = telebot.types.KeyboardButton('Share')
    button2 = telebot.types.KeyboardButton("Don't share")
    markup.row(button1)
    markup.row(button2)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'So send me some picture', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def reply(message):
    try:
        photo_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_photo = bot.download_file(photo_info.file_path)
        time_info = datetime.datetime.today()
        if os.name == 'nt':
            photo_name = '{}_{}'.format(time_info.strftime('%Y-%m-%d_%I-%M'), message.from_user.id)
        else:
            photo_name = '{}_{}'.format(time_info.strftime('%Y-%m-%d_%I:%M'), message.from_user.id)
        print(photo_name)
        src = IMAGES_PATH + photo_name + '.jpg'
        with open(src, 'wb') as new_photo:
            new_photo.write(downloaded_photo)
        bot.send_message(message.chat.id, 'You can press the "Share"-button to share your picture',
                         reply_markup=gen_share_markup())
    except:
        bot.send_message(message.chat.id, 'Something gone wrong')


if __name__ == '__main__':
    bot.infinity_polling()
