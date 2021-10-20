from telegram import InlineKeyboardMarkup

from utils.lang import text
from utils.keyboard import keyboard_proficiency
from utils.key_to_stat import get_stat
from utils.get_active import get_active
from utils.db import connect


def proficiency(update, context):

    char_id = get_active(update.message.from_user.id)

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    context.user_data.update({"char_id": char_id})

    keyboard = keyboard_proficiency()
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text("proficiency_start"), reply_markup=reply_markup)


def proficiency_button(update, context):

    c_query = update.callback_query
    choice = c_query.data[5:]

    stat_name = get_stat(choice)[0]

    if stat_name == "end":
        context.user_data.clear()
        message = text("proficiency_end")
        c_query.edit_message_text(message)
        return

    char_id = context.user_data["char_id"]

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "UPDATE `character` SET {} = not {} WHERE char_id = %s ".format(stat_name, stat_name)

    try:
        cursor.execute(query, (char_id,))
        db.commit()
    except:
        print("can not change character proficiency")

    query = "SELECT {} FROM `character` WHERE char_id = %s".format(stat_name)

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever character proficiency after update")

    result = cursor.fetchall()

    if result == [('\x00',)]:
        message = text("proficiency_false")
    else:
        message = text("proficiency_true")

    keyboard = keyboard_proficiency()
    reply_markup = InlineKeyboardMarkup(keyboard)

    c_query.edit_message_text(message.format(stat_name.replace("_", " ").upper()), reply_markup=reply_markup)
