from random import randint

from telegram import InlineKeyboardMarkup

from utils.get_active import get_active
from utils.lang import text
from utils.keyboard import keyboard_attack
from utils.db import connect


def attack(update, context):
    char_id = get_active(update.message.from_user.id)

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    keyboard = keyboard_attack()

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.user_data.update({"char_id": char_id})

    update.message.reply_text(text("attack_init"), reply_markup=reply_markup)


def attack_button(update, context):
    query = update.callback_query
    choice = query.data[7:]
    char_id = context.user_data["char_id"]

    db = connect()
    cursor = db.cursor(prepared=True)

    if choice == "melee":

        sql_query = "SELECT char_name, strength FROM `character` WHERE char_id = %s"

    elif choice == "ranged":

        sql_query = "SELECT char_name, dexterity FROM `character` WHERE char_id = %s"

    else:

        sql_query = "SELECT char_name, intelligence, wisdom, charisma FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(sql_query, (char_id,))
    except:
        print("can not retriever character stats for attack")

    result = cursor.fetchall()
    char_name = result[0][0]
    d20 = randint(1, 20)

    if choice == "melee":

        str_mod = result[0][1] // 2 - 5
        message = text("attack_melee").format(char_name, d20, str_mod, d20 + str_mod)

    elif choice == "ranged":

        dex_mod = result[0][1] // 2 - 5
        message = text("attack_ranged").format(char_name, d20, dex_mod, d20 + dex_mod)

    else:

        int_mod = result[0][1] // 2 - 5
        wis_mod = result[0][2] // 2 - 5
        cha_mod = result[0][3] // 2 - 5

        message = text("attack_spell").format(char_name,
                                              d20, int_mod, d20+int_mod,
                                              d20, wis_mod, d20+wis_mod,
                                              d20, cha_mod, d20+cha_mod)

    context.user_data.clear()

    query.edit_message_text(text=message)
