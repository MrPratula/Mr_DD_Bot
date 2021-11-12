from telegram import InlineKeyboardMarkup

from utils.lang import text
from utils.get_active import get_active, get_name
from utils.keyboard import keyboard_class
from utils.db import connect


def char_class(update, context):

    try:
        char_id = get_active(update.message.from_user.id)
    except:
        char_id = context.user_data["char_selected"]

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    char_name = get_name(char_id)

    context.user_data.update({"char_id": char_id})
    context.user_data.update({"char_name": char_name})

    db = connect()
    cursor = db.cursor(prepared=True)
    query = "SELECT name FROM class"

    try:
        cursor.execute(query, ())
    except:
        print("can not retriever class names")

    result = cursor.fetchall()

    keyboard = keyboard_class(result)
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = text("class_start").format(char_name.capitalize())

    try:
        update.message.reply_text(message, reply_markup=reply_markup)
    except:
        c_query = update.callback_query
        c_query.edit_message_text(message, reply_markup=reply_markup)


def class_select(update, context):

    c_query = update.callback_query
    class_click = c_query.data[6:]
    char_id = context.user_data["char_id"]
    char_name = context.user_data["char_name"]

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "UPDATE `character` SET class = %s WHERE char_id = %s "

    try:
        cursor.execute(query, (class_click, char_id))
        db.commit()
    except:
        print("can not update character class")

    context.user_data.clear()
    message = text("class_update").format(class_click.capitalize(), char_name.capitalize())
    c_query.edit_message_text(message)
