import telebot
import os
import logging
import datetime
from random import choice
from PIL import Image, ImageDraw, ImageFont

BOT_TOKEN = os.getenv('BOT_TOKEN')
IMAGES_PATH = os.getenv('IMAGES_PATH')
PHRASES = os.getenv('PHRASES')
CHANNEL_TO_REPOST = os.getenv('CHANNEL_TO_REPOST')

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(
    level=logging.DEBUG,
    format=''
)


def gen_share_markup():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    button = telebot.types.InlineKeyboardButton('Share', callback_data='share_photo')
    markup.add(button)
    return markup


def get_random_text(phrases_file):
    with open(phrases_file, 'r') as phrase:
        phrase = choice(phrase.read().splitlines()).encode('utf-8')
        return phrase.decode('utf-8')


def photo_draw_text(photo):
    f = open(photo, 'rb')
    with Image.open(f).convert('RGBA') as photo_to_sign:
        text = get_random_text(PHRASES)
        drw = ImageDraw.Draw(photo_to_sign)
        width_text, height_text = drw.textsize(text)
        text_size = photo_to_sign.size[0] // width_text + 10
        font = ImageFont.truetype('Lobster-Regular.ttf', size=text_size, encoding='utf-8')
        drw.text(
            ((photo_to_sign.size[0] - width_text) / 2, photo_to_sign.size[1] / 10 * 9 - height_text),
            text,
            font=font,
            fill=(0, 0, 0, 0)
        )
        return photo_to_sign


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'So send me some picture', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def reply_picture(message):
    try:
        photo_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_photo = bot.download_file(photo_info.file_path)
        time_info = datetime.datetime.today()
        if os.name == 'nt':
            photo_name = '{}_{}'.format(time_info.strftime('%Y-%m-%d_%I-%M'), message.from_user.id)
        else:
            photo_name = '{}_{}'.format(time_info.strftime('%Y-%m-%d_%I:%M'), message.from_user.id)
        src = IMAGES_PATH + photo_name + '.jpg'
        with open(src, 'wb') as new_photo:
            new_photo.write(downloaded_photo)
        signed_photo = photo_draw_text(src)
        bot.send_photo(message.chat.id, signed_photo, reply_markup=gen_share_markup())
    except Exception as e:
        print(str(e))
        bot.send_message(message.chat.id, 'Something gone wrong')


@bot.callback_query_handler(func=lambda call: True)
def callback_query_repost_photo(inline_call):
    if inline_call.data == 'share_photo':
        bot.answer_callback_query(inline_call.id, 'Photo shared')
        bot.forward_message(CHANNEL_TO_REPOST, inline_call.from_user.id, inline_call.message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()
