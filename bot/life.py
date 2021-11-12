

from telegram import InlineKeyboardMarkup

from utils.keyboard import keyboard_life
from utils.get_active import get_active, get_hp, get_name, update_life
from utils.lang import text


def life(update, context):

    try:
        char_id = get_active(update.message.from_user.id)
    except:
        char_id = context.user_data["char_selected"]

    char_hp = get_hp(char_id)
    char_name = get_name(char_id)

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    keyboard = keyboard_life(char_hp)

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.user_data.update({"char_id": char_id})
    context.user_data.update({"char_hp": char_hp})
    context.user_data.update({"char_name": char_name})

    message = text("life_init").format(char_name.capitalize())

    try:
        update.message.reply_text(message, reply_markup=reply_markup)
    except:
        c_query = update.callback_query
        c_query.edit_message_text(message, reply_markup=reply_markup)


def life_button(update, context):

    query = update.callback_query
    choice = query.data[5:]
    char_id = context.user_data["char_id"]
    char_hp = context.user_data["char_hp"]
    char_name = context.user_data["char_name"]

    if choice == "up":
        char_hp += 1
        update_life(char_id, char_hp)
        context.user_data.update({"char_hp": char_hp})
        message = text("life_up").format(char_name.capitalize())

    elif choice == "down":
        char_hp -= 1
        update_life(char_id, char_hp)
        context.user_data.update({"char_hp": char_hp})
        message = text("life_down").format(char_name.capitalize())

    elif choice == "end":
        message = text("life_end").format(char_name.capitalize())
        context.user_data.clear()
        query.edit_message_text(message)
        return

    else:
        return

    keyboard = keyboard_life(char_hp)
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(message, reply_markup=reply_markup)
