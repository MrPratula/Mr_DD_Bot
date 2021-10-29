

from telegram import InlineKeyboardMarkup

from utils.get_active import get_active, get_name
from utils.lang import text
from utils.keyboard import keyboard_config, keyboard_config_2
from utils.db import connect


def config(update, context):

    char_id = get_active(update.message.from_user.id)

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    char_name = get_name(char_id)

    context.user_data.update({"char_id": char_id})
    context.user_data.update({"char_name": char_name})

    keyboard = keyboard_config()
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = text("config_start").format(char_name).capitalize()

    update.message.reply_text(message, reply_markup=reply_markup)


def config_first_button(update, context):

    c_query = update.callback_query
    choice = c_query.data[9:]
    char_id = context.user_data["char_id"]

    db = connect()
    cursor = db.cursor(prepared=True)

    if choice == "spell":
        query_1 = "SELECT name FROM cantrip"
        query_2 = "SELECT spell_name FROM has_spell WHERE char_id = %s"
        message = text("config_spell_1")

    else:
        query_1 = "SELECT name FROM weapons"
        query_2 = "SELECT weapon FROM has_weapon WHERE char_id = %s"
        message = text("config_weapon_1")

    try:
        cursor.execute(query_1, ())
    except:
        print("can not retriever spells or weapons names list")

    result_1 = cursor.fetchall()

    try:
        cursor.execute(query_2, (char_id,))
    except:
        print("can not retriever spells or weapons names list")

    result_2 = cursor.fetchall()

    keyboard = keyboard_config_2(result_1, result_2, choice)

    reply_markup = InlineKeyboardMarkup(keyboard)
    c_query.edit_message_text(message, reply_markup=reply_markup)


def config_spell_button(update, context):

    c_query = update.callback_query
    spell_click = c_query.data[15:]
    char_id = context.user_data["char_id"]

    if spell_click == "end":
        char_name = context.user_data["char_name"]
        message = text("config_spell_end").format(char_name).capitalize()
        context.user_data.clear()
        c_query.edit_message_text(message)
        return

    db = connect()
    cursor = db.cursor(prepared=True)
    query = "DELETE FROM has_spell WHERE char_id = %s AND spell_name = %s"

    try:
        cursor.execute(query, (char_id, spell_click))
        db.commit()
    except:
        print("can not delete spell from has_spell")

    if cursor.rowcount == 0:

        query = "INSERT INTO has_spell (char_id, spell_name) VALUES (%s, %s)"

        try:
            cursor.execute(query, (char_id, spell_click))
            db.commit()
        except:
            print("can not delete add spell into has_spell")

    query_1 = "SELECT name FROM cantrip"
    query_2 = "SELECT spell_name FROM has_spell WHERE char_id = %s"

    try:
        cursor.execute(query_1, ())
    except:
        print("can not retriever spells names list")

    result_1 = cursor.fetchall()

    try:
        cursor.execute(query_2, (char_id,))
    except:
        print("can not retriever spells names list")

    result_2 = cursor.fetchall()

    keyboard = keyboard_config_2(result_1, result_2, "spell")

    message = text("config_spell_1")

    reply_markup = InlineKeyboardMarkup(keyboard)
    c_query.edit_message_text(message, reply_markup=reply_markup)


def config_weap_button(update, context):

    c_query = update.callback_query
    weapon_click = c_query.data[14:]
    char_id = context.user_data["char_id"]

    if weapon_click == "end":
        char_name = context.user_data["char_name"]
        message = text("config_weap_end").format(char_name).capitalize()
        context.user_data.clear()
        c_query.edit_message_text(message)
        return

    db = connect()
    cursor = db.cursor(prepared=True)
    query = "DELETE FROM has_weapon WHERE char_id = %s AND weapon = %s"

    try:
        cursor.execute(query, (char_id, weapon_click))
        db.commit()
    except:
        print("can not delete weapon from has_weapon")

    if cursor.rowcount == 0:

        query = "INSERT INTO has_weapon (char_id, weapon) VALUES (%s, %s)"

        try:
            cursor.execute(query, (char_id, weapon_click))
            db.commit()
        except:
            print("can not delete add spell into has_spell")

    query_1 = "SELECT name FROM weapons"
    query_2 = "SELECT weapon FROM has_weapon WHERE char_id = %s"

    try:
        cursor.execute(query_1, ())
    except:
        print("can not retriever weapons names list")

    result_1 = cursor.fetchall()

    try:
        cursor.execute(query_2, (char_id,))
    except:
        print("can not retriever weapons names list")

    result_2 = cursor.fetchall()

    keyboard = keyboard_config_2(result_1, result_2, "weap")

    message = text("config_weapon_1")

    reply_markup = InlineKeyboardMarkup(keyboard)
    c_query.edit_message_text(message, reply_markup=reply_markup)
