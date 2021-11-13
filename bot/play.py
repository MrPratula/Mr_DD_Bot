
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from utils.lang import text


def play(update, context):

    keyboard = [["/roll", "/check", "/attack"],
                ["/close"]]

    placeholder = text("play_placeholder")
    message = text("play_start")

    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=False,
                                       resize_keyboard=True, input_field_placeholder=placeholder)

    update.message.reply_text(message, reply_markup=reply_markup)


def close(update, context):

    message = text("play_close")
    update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
