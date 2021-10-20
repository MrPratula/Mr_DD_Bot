from random import randint

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils.lang import text
from utils.keyboard import keyboard_die


def roll(update, context):

    keyboard = keyboard_die()
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text("roll_menu"), reply_markup=reply_markup)


def button_roll(update, context):

    query = update.callback_query
    val = int(query.data[2:])

    result = randint(1, val)
    message = text("roll_result").format(val, result)

    query.answer()
    query.edit_message_text(text=message)
