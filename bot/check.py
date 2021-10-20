
from random import randint

from telegram import InlineKeyboardMarkup

from utils.db import connect
from utils.lang import text
from utils.keyboard import keyboard_ability, keyboard_sub_ability
from utils.key_to_stat import get_stat
from utils.get_active import get_active


def check(update, context):

    char_id = get_active(update.message.from_user.id)

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    keyboard = keyboard_ability()

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.user_data.update({"char_id": char_id})

    update.message.reply_text(text("check_first"), reply_markup=reply_markup)


def first_check_button(update, context):

    query = update.callback_query
    choice = query.data[7:]

    keyboard = keyboard_sub_ability(choice)
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=text("check_first"), reply_markup=reply_markup)


def second_check_button(update, context):

    query = update.callback_query
    choice = query.data[7:]
    char_id = context.user_data["char_id"]

    data = get_modifier(choice, char_id)

    if data is None:
        message = text("check_deleted_character")
        context.user_data.clear()
        query.edit_message_text(text=message)
        return

    name = data[0]
    mod = data[1]
    word = data[2].replace("_", " ").upper()

    roll = randint(1, 20)

    message = text("check_last")
    context.user_data.clear()

    query.edit_message_text(text=message.format(name, word, roll, mod, roll+mod))


def get_modifier(choice, char_id):

    db = connect()
    cursor = db.cursor(prepared=True)

    stat_name = get_stat(choice)[0]
    main_stat_name = get_stat(choice)[1]

    if stat_name == main_stat_name:

        query = "SELECT char_name, {} FROM `character` WHERE char_id = %s".format(stat_name)

        try:
            cursor.execute(query, (char_id,))
        except:
            print("can not get stat from character for check")

        result = cursor.fetchall()

        try:
            name = result[0][0]
        except IndexError:
            return None

        stat = int(result[0][1])

        return [name, (stat//2)-5, stat_name]

    else:

        query = "SELECT char_name, {}, {}, proficiency FROM `character` WHERE char_id = %s"\
                .format(stat_name, main_stat_name)

        try:
            cursor.execute(query, (char_id,))
        except:
            print("can not get stat from character for check")

        result = cursor.fetchall()

        try:
            name = result[0][0]
        except IndexError:
            return None

        if result[0][1] == '\x00':
            have_proficiency = False
        else:
            have_proficiency = True

        stat = int(result[0][2])
        proficiency = int(result[0][3])

        if have_proficiency:
            return [name, (stat//2)-5+proficiency, stat_name]
        else:
            return [name, (stat//2)-5, stat_name]
