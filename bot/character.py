import telegram

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from utils.lang import text
from utils.db import connect
from utils.key_to_stat import get_stat, stat_name, prof_name
from utils.keyboard import keyboard_edit


def character(update, context):

    db = connect()
    cursor = db.cursor(prepared=True)
    query = "SELECT char_name, own.char_id " \
            "FROM own, `character` " \
            "WHERE own.user_id = %s and own.char_id = `character`.char_id"

    chat_id = update.message.from_user.id

    keyboard = []

    try:
        cursor.execute(query, (chat_id,))
    except:
        print("query failed")

    result = cursor.fetchall()

    if not result:

        message = text("char_none")
        context.bot.send_message(chat_id=chat_id, text=message)

    else:
        for name in result:

            keyboard.append([InlineKeyboardButton(name[0], callback_data="char_view_" + str(name[1]))])

            keyboard.append([InlineKeyboardButton("✅", callback_data="char_active_" + str(name[1])),
                             InlineKeyboardButton("🔧", callback_data="char_edit_" + str(name[1])),
                             InlineKeyboardButton("❌", callback_data="char_delete_" + str(name[1]))])

            context.user_data.update({name[1]: name[0]})

        keyboard.append([InlineKeyboardButton("🔴   CLOSE   🔴", callback_data="char_close")])

        context.user_data.update({"user": chat_id})

        message = text("char_some")

        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)


def char_view_button(update, context):

    c_query = update.callback_query
    char_id = int(c_query.data[10:])
    char_name = context.user_data[char_id]

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "SELECT strength, dexterity, constitution, intelligence, wisdom, charisma, proficiency " \
            "FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever char_id from active")

    result_stat = cursor.fetchall()

    query = "SELECT strength_saving_throw, athletics, dexterity_saving_throw, acrobatics, sleight_of_hand, stealth, " \
            "       constitution_saving_throw, intelligence_saving_throw, arcana, history, investigation, nature, " \
            "       religion, wisdom_saving_throw, animal_handling, insight, medicine, perception, survival, " \
            "       charisma_saving_throw, deception, intimidation, performance, persuasion " \
            "FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever char_id from active")

    result_prof = cursor.fetchall()

    stats = []
    for stat in result_stat[0]:
        stats.append(stat)

    profs = []
    pos = 0
    for prof in result_prof[0]:
        if prof == '\x01':
            profs.append(prof_name(pos))
            pos += 1

    char_name = "<b>"+char_name+"</b>"
    message = text("char_view").format(char_name, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6],
                                       " - ".join(profs).replace("_", " "))
    c_query.edit_message_text(text=message, parse_mode=telegram.ParseMode.HTML)


def char_active_button(update, context):

    query = update.callback_query

    char_id = int(query.data[12:])
    char_name = context.user_data[char_id]

    chat_id = context.user_data["user"]

    db = connect()
    cursor = db.cursor(prepared=True)
    sql_query = "UPDATE active SET char_id = %s WHERE chat_id = %s"
    val = (char_id, chat_id)

    try:
        cursor.execute(sql_query, val)
        db.commit()
    except:
        print("can not update active character")

    message = text("char_update").format(char_name)

    query.answer()
    context.user_data.clear()
    query.edit_message_text(text=message)


def char_edit_button(update, context):

    c_query = update.callback_query

    char_id = int(c_query.data[10:])
    context.user_data.update({"char_selected": char_id})
    context.user_data.update({"char_id": char_id})
    char_name = context.user_data[char_id]
    context.user_data.update({"char_name": char_name})

    keyboard = keyboard_edit()

    message = text("char_edit").format(char_name)
    reply_markup = InlineKeyboardMarkup(keyboard)

    c_query.edit_message_text(text=message, reply_markup=reply_markup)


def char_edit_stats_button(update, context):

    c_query = update.callback_query

    char_id = context.user_data["char_selected"]
    char_name = context.user_data[char_id]

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "SELECT strength, dexterity, constitution, intelligence, wisdom, charisma, proficiency " \
            "FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever character stats")

    result_stat = cursor.fetchall()

    keyboard = []
    var = 0
    for stat in result_stat[0]:
        name = stat_name(var)
        keyboard.append([InlineKeyboardButton("➖", callback_data="char_stat_{}_dn".format(name)),
                         InlineKeyboardButton("{} = {}".format(name, stat), callback_data="char_stat_none"),
                         InlineKeyboardButton("➕", callback_data="char_stat_{}_up".format(name))])
        var += 1
    keyboard.append([InlineKeyboardButton("✅   SAVE   ✅", callback_data="char_stat_end")])

    message = text("char_stat").format(char_name)
    reply_markup = InlineKeyboardMarkup(keyboard)

    c_query.edit_message_text(text=message, reply_markup=reply_markup)


def char_stat_button(update, context):

    c_query = update.callback_query
    char_id = context.user_data["char_selected"]
    char_name = context.user_data[char_id]
    key = c_query.data[10:]

    if key == "end":
        context.user_data.clear()
        c_query.edit_message_text(text=text("char_edit_complete"))
        return

    stat = key[:3]
    what = key[4:]
    word = get_stat(stat.lower())[0]

    db = connect()
    cursor = db.cursor(prepared=True)

    if what == "up":
        query = "UPDATE `character` SET {} = {} +1 WHERE char_id = %s ".format(word, word)
    else:
        query = "UPDATE `character` SET {} = {} -1 WHERE char_id = %s ".format(word, word)

    try:
        cursor.execute(query, (char_id,))
        db.commit()
    except:
        print("can not change character stat")

    query = "SELECT strength, dexterity, constitution, intelligence, wisdom, charisma, proficiency " \
            "FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever character stats")

    result_stat = cursor.fetchall()

    keyboard = []
    var = 0
    for stat in result_stat[0]:
        name = stat_name(var)
        keyboard.append([InlineKeyboardButton("➖", callback_data="char_stat_{}_dn".format(name)),
                         InlineKeyboardButton("{} = {}".format(name, stat), callback_data="char_stat_none"),
                         InlineKeyboardButton("➕", callback_data="char_stat_{}_up".format(name))])
        var += 1
    keyboard.append([InlineKeyboardButton("✅   SAVE   ✅", callback_data="char_stat_end")])

    message = text("char_stat").format(char_name)
    reply_markup = InlineKeyboardMarkup(keyboard)

    c_query.edit_message_text(text=message, reply_markup=reply_markup)


def char_delete_button(update, context):

    c_query = update.callback_query

    char_id = int(c_query.data[12:])
    char_name = context.user_data[char_id]

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "DELETE FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
        db.commit()
    except:
        print("can not delete character")

    c_query.edit_message_text(text=text("char_delete").format(char_name))


def char_close(update, context):

    c_query = update.callback_query
    context.user_data.clear()
    c_query.edit_message_text(text=text("char_close"))
