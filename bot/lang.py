import json

from telegram import InlineKeyboardMarkup

from utils.keyboard import keyboard_language
from utils.lang import text


def language(update, context):

    keyboard = keyboard_language()

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Please, select a language", reply_markup=reply_markup)


def language_button(update, context):

    query = update.callback_query
    choice = query.data[5:]

    with open("lang/config.json", "r+") as f_config:
        config_dict = json.load(f_config)
        config_dict.update({"language": choice})
        f_config.seek(0)
        json.dump(config_dict, f_config, indent=4)
        f_config.truncate()

    query.edit_message_text(text("lang_update"))
